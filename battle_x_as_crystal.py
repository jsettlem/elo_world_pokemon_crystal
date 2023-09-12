import os
import random
import shutil
import string
from io import BytesIO

from pyboy import PyBoy

import constants.file_paths as files
from constants.memory import wEnemyTrainerItems
from utils.battle_logger import start_new_battle, end_battle, add_turn, make_batch
from utils.battle_printer import print_battle_log
from utils.bgb import call_bgb
from utils.data import *
from utils.demos import *
from utils.files import *
from utils.hashids import encode_battle, decode_battle
from utils.movies import build_movie, MovieContext
from utils.pyboy_util import set_value, run_until_breakpoint, copy_values, get_value, randomize_rdiv


def load_trainer_info(trainer_class: int, trainer_id: int, emulator: PyBoy, save: bytes):

	emulator.load_state(BytesIO(save))

	set_value(emulator, [trainer_class], memory.wOtherTrainerClass)
	set_value(emulator, [trainer_id], memory.wOtherTrainerID)

	run_until_breakpoint(emulator, ['PlaceCommandCharacter'])


def set_up_battle_emulator(base_save: bytearray, primary_emulator: PyBoy, work_emulator: PyBoy, enemy_class: int,
						   enemy_index: int, player_gender: str, rng: random.Random):
	# work_emulator contains the loaded player trainer data
	# primary_emulator should be initialized to the start of the battle

	primary_emulator.load_state(BytesIO(base_save))

	copy_values(work_emulator, memory.wOTParty, primary_emulator, memory.wPlayerParty)

	enemy_party_size = get_value(work_emulator, memory.wOTPartyCount)[0]

	for i in range(enemy_party_size):
		pokemon = get_value(work_emulator, memory.enemyParty[i])
		pokemon_index = pokemon[0] - 1
		pokemon_name = name_to_bytes(pokemon_names[str(pokemon_index)])
		set_value(primary_emulator, pokemon_name, memory.playerPartyNicks[i])
		copy_values(work_emulator, memory.wStringBuffer1, primary_emulator, memory.playerPartyOTs[i])

	copy_values(work_emulator, memory.wStringBuffer1, primary_emulator, memory.wPlayerName)
	set_value(primary_emulator, [memory.NAME_TERMINATOR], memory.playerNameEnd)

	if player_gender == "FEMALE" or (player_gender == "ENBY" and rng.random() > 0.5):
		set_value(primary_emulator, [0x1], memory.wPlayerGender)

	set_value(primary_emulator, [enemy_class], memory.wOtherTrainerClass)
	set_value(primary_emulator, [enemy_class], memory.wTrainerClass)
	set_value(primary_emulator, [enemy_index], memory.wOtherTrainerID)

	randomize_rdiv(primary_emulator, rng)

	# randomize textbox frame
	set_value(primary_emulator, [rng.randint(0, 8)], memory.wTextboxFrame)

	set_value(primary_emulator, [0x1], memory.wNumItems)
	item_id = memory.itemXAttack
	set_value(primary_emulator, [item_id, 0x1, 0xff], memory.wItems)


def get_ai_action(primary_emulator: PyBoy, base_save: str, working_emulator: PyBoy, trainer: Tuple[int, int],
                  rng: random.Random, current_player_items: bytearray = None):
	ai_save = load_save(base_save)
	working_emulator.load_state(BytesIO(ai_save))
	swap_pairings(primary_emulator, working_emulator)

	set_value(working_emulator, [0b1], memory.wTextboxFlags)

	set_value(working_emulator, [trainer[0]], memory.wOtherTrainerClass)
	set_value(working_emulator, [trainer[0]], memory.wTrainerClass)
	set_value(working_emulator, [trainer[1]], memory.wOtherTrainerID)

	# Edge case -- the AI gets confused if the player mon has no HP
	if get_value(primary_emulator, memory.wEnemyMonHP) == b"\x00\x00":
		print("It's zero!")
		set_value(working_emulator, [0x0, 0x1], memory.wBattleMonHP)

	randomize_rdiv(working_emulator, rng)

	if current_player_items is not None:
		set_value(working_emulator, current_player_items, memory.wEnemyTrainerItems)

	set_value(working_emulator, get_enemy_used_moves(primary_emulator), memory.wPlayerUsedMoves)

	copy_values(primary_emulator, memory.wBattleWeather, working_emulator, memory.wBattleWeather)

	# This is to work around a bug in the actual game that normally never triggers
	# See https://twitter.com/pimanrules/status/1528137472680640513
	set_value(working_emulator, [0x0], memory.wEnemyTrainerBaseReward)

	# TODO: we may need to update more values here. Check the disassembly.

	# These allow us to make the game think our Pokemon is always on the last turn of Perish Song
	# set_value(ai_save, wEnemySubStatus1[0], [0x10], 1)
	# set_value(ai_save, wEnemyPerishCount[0], [0x1], 1)

	run_until_breakpoint(working_emulator,
		 breakpoints=[
			 # for switching:
			 'LoadEnemyMon',
			 # for move selection:
			 'PlayerTurn_EndOpponentProtectEndureDestinyBond', 'EnemyTurn_EndOpponentProtectEndureDestinyBond',
			 'AI_Switch',
			 'EnemyUsedFullHeal', 'EnemyUsedMaxPotion', 'EnemyUsedFullRestore', 'EnemyUsedPotion', 'EnemyUsedSuperPotion',
			 'EnemyUsedHyperPotion', 'EnemyUsedXAccuracy', 'EnemyUsedGuardSpec', 'EnemyUsedDireHit', 'EnemyUsedXAttack',
			 'EnemyUsedXDefend', 'EnemyUsedXSpeed', 'EnemyUsedXSpecial',
		 ], demo=generate_ai_demo())


def swap_pairings(source_emulator: PyBoy, target_emulator: PyBoy):
	# Copy data from battle save to ai save, swapping the player and enemy data

	for pairing in memory.player_enemy_pairs:
		player_address, enemy_address = pairing

		copy_values(source_emulator, player_address, target_emulator, enemy_address)
		copy_values(source_emulator, enemy_address, target_emulator, player_address)


def get_enemy_used_moves(primary_emulator: PyBoy)  -> bytearray:
	# wPlayerUsed moves keeps track of the moves the enemy has seen the player use.
	# There's no equivalent for the enemy's moves, so this is a bit of a hack, looking for moves that aren't at full PP.
	# There are some edge cases where this fails, but they're relatively rare and this isn't used much anyway:
	# - If the enemy uses transform (they'll all be at less-than-full PP)
	# - If the enemy uses struggle (it should bump something off the list, but it won't)
	# - If the enemy switches out and back in (it should reset the list, but it won't reset PP)
	# - If the enemy uses a MysteryBerry (fortunately, no trainers do)
	# For completion's sake, some edge-cases that don't matter because enemies aren't players:
	# - If the enemy learns a move in the middle of battle (can happen for player Pokémon)
	# - If the enemy has used a PP Up
	# - If the enemy uses Sketch (no enemies have Smeargle)
	used_move_list = bytearray([0, 0, 0, 0])
	enemy_moves = get_value(primary_emulator, memory.wEnemyMonMoves)
	enemy_pp = get_value(primary_emulator, memory.wEnemyMonPP)
	for i, move in enumerate(enemy_moves):
		if move != 0:
			expected_pp = moves[move]["pp"]
			if enemy_pp[i] != expected_pp:
				used_move_list[used_move_list.index(0)] = move
	return used_move_list


def get_battle_mons(battle_save: PyBoy) -> Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int]]:
	return (
		(
			get_value(battle_save, memory.wBattleMonSpecies)[0],
			get_stat(get_value(battle_save, memory.wBattleMonHP)),
			get_stat(get_value(battle_save, memory.wBattleMonMaxHP)),
			get_value(battle_save, memory.wCurPartyMon)[0]
		),
		(
			get_value(battle_save, memory.wEnemyMonSpecies)[0],
			get_stat(get_value(battle_save, memory.wEnemyMonHP)),
			get_stat(get_value(battle_save, memory.wEnemyMonMaxHP)),
			get_value(battle_save, memory.wCurOTMon)[0]
		)
	)


def run_one_battle(player_trainer, enemy_trainer, run_identifier, save_movie=False):
	rng = random.Random(run_identifier)

	# Set up working directory

	directory_nonce = str(rng.randint(0, 999999999))

	working_dir = os.path.abspath(f"{files.SCRATCH_DIR}/{run_identifier}")
	output_dir = os.path.abspath(f"{files.OUT_DIR}/{run_identifier}")
	movie_working_dir = f"{working_dir}/movie_{directory_nonce}"
	movie_context = MovieContext(movie_name=str(run_identifier),
	                             movie_index=0,
	                             movie_working_dir=movie_working_dir,
	                             movie_output_dir=output_dir) if save_movie else None

	# for directory in [working_dir, movie_working_dir]:
	# 	os.makedirs(directory, exist_ok=True)

	player_class = player_trainer['class']
	player_index = player_trainer['instance']
	enemy_class = enemy_trainer['class']
	enemy_index = enemy_trainer['instance']

	battle_log = start_new_battle(seed=run_identifier,
	                              player=(player_class, player_index),
	                              enemy=(enemy_class, enemy_index))

	base_save = load_save(files.BASE_SAVE)
	base_ai_save = load_save(files.BASE_AI_SAVE)
	base_switch_save = load_save(files.BASE_SWITCH_SAVE)

	work_emulator = get_pyboy_instance(headless=True)
	# work_emulator = get_pyboy_instance(headless=False)
	primary_emulator = get_pyboy_instance(headless=True)
	# primary_emulator = get_pyboy_instance(headless=False)

	# Load the data for the player trainer
	load_trainer_info(player_class, player_index, work_emulator, base_save)

	# return fetch_trainer_party_moves(player_trainer_info)

	# Set up the initial battle state
	set_up_battle_emulator(base_save, primary_emulator, work_emulator, enemy_class, enemy_index, player_trainer["gender"], rng)

	current_player_items = get_value(work_emulator, wEnemyTrainerItems)

	# write_file(battle_save_path, battle_save)
	# write_file(out_demo_path, generate_demo([]))

	turn_count = 0

	button_sequence = generate_demo([])

	while True:
		# Play until we reach a menu or win/lose
		# total_clocks = battle_save.get_total_clocks()
		# breakpoint_condition = f"TOTALCLKS!=${total_clocks:x}"
		run_until_breakpoint(primary_emulator, breakpoints=[
			"BattleMenu",
			"SetUpBattlePartyMenu",
			"WinTrainerBattle",
			"LostBattle",
		], demo=button_sequence)

		player_battle_mon, enemy_battle_mon = get_battle_mons(primary_emulator)

		pc = primary_emulator.mb.cpu.PC

		# Which breakpoint did we hit?
		if pc == memory.breakpoints["WinTrainerBattle"]:
			# Player won!
			end_battle(battle_log, "PLAYER")
			break
		elif pc == memory.breakpoints["LostBattle"]:
			# Enemy won!
			end_battle(battle_log, "ENEMY")
			break
		elif pc == memory.breakpoints["SetUpBattlePartyMenu"]:
			# AI is forced to switch out, what should we switch to?

			get_ai_action(primary_emulator=primary_emulator,
			                          base_save=files.BASE_SWITCH_SAVE,
			                          working_emulator=work_emulator,
			                          trainer=(player_class, player_index),
			                          rng=rng)

			target_pokemon = get_value(work_emulator, memory.wCurPartyMon)[0]  # should this be wCurBattleMon? probably...
			current_pokemon_index = get_current_pokemon_index(primary_emulator)

			button_sequence = choose_pokemon(current_pokemon_index, target_pokemon)
			add_turn(battle_log, "FORCE_SWITCH", target_pokemon, player_battle_mon, enemy_battle_mon)
		else:
			# We're at the battle menu, what should we choose?

			get_ai_action(primary_emulator=primary_emulator,
			                          base_save=files.BASE_AI_SAVE,
									  working_emulator=work_emulator,
			                          trainer=(player_class, player_index),
			                          current_player_items=current_player_items,
			                          rng=rng)

			ai_pc = work_emulator.mb.cpu.PC
			if ai_pc in memory.items.keys():
				set_value(primary_emulator, [0x1], memory.wNumItems)
				item_id = memory.items[ai_pc]
				set_value(primary_emulator, [item_id, 0x1, 0xff], memory.wItems)

				target_pokemon = get_value(primary_emulator, memory.wCurBattleMon)[0]
				current_pokemon_index = get_current_pokemon_index(primary_emulator)

				button_sequence = select_item(current_pokemon_index, target_pokemon)

				current_player_items[current_player_items.index(item_id)] = 0x0

				add_turn(battle_log, "ITEM", item_id, player_battle_mon, enemy_battle_mon)

			elif ai_pc == memory.breakpoints["AI_Switch"]:
				target_pokemon = get_value(work_emulator, memory.wEnemySwitchMonIndex)[0] - 1
				current_pokemon_index = get_current_pokemon_index(primary_emulator)

				button_sequence = select_switch() + choose_pokemon(current_pokemon_index, target_pokemon)

				add_turn(battle_log, "SWITCH", target_pokemon, player_battle_mon, enemy_battle_mon)

			else:
				selected_move_index = get_value(work_emulator, memory.wCurEnemyMoveNum)[0]
				current_move_index = get_value(primary_emulator, memory.wCurMoveNum)[0]

				button_sequence = select_move(current_move_index, selected_move_index)

				# TODO: how does struggle work?
				player_moves = get_value(primary_emulator, memory.wBattleMonMoves)

				add_turn(battle_log, "MOVE", player_moves[selected_move_index], player_battle_mon, enemy_battle_mon)

		turn_count += 1

	if save_movie:
		os.makedirs(output_dir, exist_ok=True)
		build_movie(movie_context)

	# for created_dir in [movie_working_dir]:
	# 	shutil.rmtree(created_dir)
	# os.rmdir(working_dir)

	work_emulator.stop(save=False)
	primary_emulator.stop(save=False)

	return battle_log



def get_pyboy_instance(headless=True):
	if headless:
		emulator = PyBoy(
			files.ROM_IMAGE,
			window_type="dummy",
			randomize=False,
			disable_renderer=True,
		)
	else:
		emulator = PyBoy(
			files.ROM_IMAGE,
			randomize=False,
			sound=True,
		)
		emulator.set_emulation_speed(0)

	return emulator


def run_random_battle(seed=None, save_movie=False):
	if seed is None:
		seed = str(random.randint(0, 2 ** 32))
	rng = random.Random(seed)
	print("rng seed", seed)

	player_trainer, enemy_trainer = rng.choice(raw_trainer_data), rng.choice(raw_trainer_data)

	return run_battle_with_trainers(enemy_trainer, player_trainer, rng, save_movie)


def run_battle_with_trainers(enemy_trainer, player_trainer, rng, save_movie=False):
	battle_nonce = rng.randint(0, 255)
	run_identifier = encode_battle(player_trainer["class"], player_trainer["instance"], enemy_trainer["class"],
	                               enemy_trainer["instance"], battle_nonce)
	battle_log = run_one_battle(player_trainer, enemy_trainer, run_identifier, save_movie=save_movie)
	return battle_log


def run_battle_from_hashid(hashid: str, save_movie=False):
	player_trainer, enemy_trainer, battle_nonce = decode_battle(hashid)
	battle_seed = hashid.replace(" ", "")
	battle_log = run_one_battle(player_trainer, enemy_trainer, battle_seed, save_movie=save_movie)
	return battle_log


def run_random_battles_batch(n=5):
	battle_logs = [run_random_battle() for _ in range(n)]
	return make_batch(battle_logs)


def test_batch_battles(n=5):
	batches = run_random_battles_batch(n=n)
	batch_out = save_battle_batch(batches, "test_batches")

	print("batch_out", batch_out)

	print("reading back batch file...")

	batches_read = load_battle_batch(batch_out)

	for battle in batches_read.battles:
		print_battle_log(battle)


def test_battles_with_all_trainers():
	for trainer in raw_trainer_data[432:]:
		seed = str(random.randint(0, 2 ** 32))
		rng = random.Random(seed)
		print("rng seed", seed)
		run_battle_with_trainers(trainer, trainer, rng, save_movie=False)

def fetch_trainer_parties():
	raw_trainer_parties = []
	for trainer in raw_trainer_data:
		party = run_one_battle(
			player_trainer=get_player_by_class_id(trainer["class"], trainer["instance"]),
			enemy_trainer=get_player_by_class_id(trainer["class"], trainer["instance"]),
			run_identifier="get_trainer_party",
		)
		raw_trainer_parties.append({'class': trainer["class"], 'instance': trainer["instance"], "moves": list(party)})

	with open("raw_trainer_movesets.json", "w") as f:
		json.dump(raw_trainer_parties, f, indent=4)

def fetch_trainer_party_moves(save: BessSave):
	party_moves = []
	party_count = save.get_value(memory.wOTPartyCount)[0]
	for i in range(party_count):
		mon_struct = save.get_value(memory.enemyParty[i])
		party_moves.append(list(mon_struct[2:6]))


	return party_moves


if __name__ == '__main__':
	# fetch_trainer_parties()
	# trainer_Blue = get_player_by_class_id(64, 1)
	# trainer_Surge = get_player_by_class_id(19, 1)
	# trainer_Will = get_player_by_class_id(11, 1)
	trainer_Cal = get_player_by_class_id(12, 3)
	# trainer_Meganium = get_player_by_class_id(42, 4)
	trainer_Blaine = get_player_by_class_id(46, 1)
	# trainer_Typhlosion = get_player_by_class_id(42, 5)
	# trainer_Reena = get_player_by_class_id(28, 20)
	# trainer_Lance = get_player_by_class_id(16, 1)
	# trainer_Claire = get_player_by_class_id(8, 1)
	trainer_Misty = get_player_by_class_id(18, 1)
	# trainer_Sabrina = get_player_by_class_id(35, 1)
	# trainer_Feraligatr = get_player_by_class_id(42, 6)
	# trainer_Koga = get_player_by_class_id(15, 1)
	# trainer_Karen = get_player_by_class_id(14, 1)
	# trainer_Bruno = get_player_by_class_id(13, 1)
	# trainer_Red = get_player_by_class_id(63, 1)
	#
	trainer_Cal1 = get_player_by_class_id(12, 1)
	trainer_Cal2 = get_player_by_class_id(12, 2)
	#
	# logs = []
	#
	# run_battle_with_trainers(trainer_Cal1, trainer_Cal1, random.Random("sweet_16_1"), save_movie=False)
	# run_battle_with_trainers(trainer_Cal2, trainer_Misty, random.Random("sweet_16_1"), save_movie=False)

	# logs.append(run_battle_with_trainers(trainer_Blue, trainer_Surge, random.Random("sweet_16_1"), save_movie=True))
	# logs.append(run_battle_with_trainers(trainer_Will, trainer_Cal, random.Random("sweet_16_1"), save_movie=True))
	# logs.append(run_battle_with_trainers(trainer_Meganium, trainer_Blaine, random.Random("sweet_16_1"), save_movie=True))
	# logs.append(
	# 	run_battle_with_trainers(trainer_Typhlosion, trainer_Reena, random.Random("sweet_16_1"), save_movie=True))
	# logs.append(run_battle_with_trainers(trainer_Lance, trainer_Claire, random.Random("sweet_16_1"), save_movie=True))
	# logs.append(run_battle_with_trainers(trainer_Misty, trainer_Sabrina, random.Random("sweet_16_1"), save_movie=True))
	# logs.append(run_battle_with_trainers(trainer_Feraligatr, trainer_Koga, random.Random("sweet_16_1"), save_movie=True))
	# logs.append(run_battle_with_trainers(trainer_Karen, trainer_Bruno, random.Random("sweet_16_1"), save_movie=True))

	# logs.append(run_battle_with_trainers(trainer_Blue, trainer_Cal, random.Random("sweet_16_2"), save_movie=True))
	# logs.append(run_battle_with_trainers(trainer_Meganium, trainer_Typhlosion, random.Random("sweet_16_2"), save_movie=True))
	# logs.append(run_battle_with_trainers(trainer_Lance, trainer_Misty, random.Random("sweet_16_2"), save_movie=True))
	# logs.append(run_battle_with_trainers(trainer_Feraligatr, trainer_Bruno, random.Random("sweet_16_2"), save_movie=True))
	# logs.append(
	# 	run_battle_with_trainers(trainer_Blue, trainer_Typhlosion, random.Random("sweet_16_3"), save_movie=True))
	# logs.append(
	# 	run_battle_with_trainers(trainer_Lance, trainer_Feraligatr, random.Random("sweet_16_3"), save_movie=True))

	# logs.append(run_battle_with_trainers(trainer_Blue, trainer_Feraligatr, random.Random("sweet_16_3"), save_movie=True))


	# for log in logs:
	# 	print(log.seed)



	# run_battle_with_trainers(trainer_Blaine, trainer_Misty, random.Random("garbagewowow"), save_movie=True)
	# run_battle_with_trainers(trainer_Misty, trainer_Blaine, random.Random("garbagewowow"), save_movie=True)

	#ditto battles
	# run_battle_with_trainers(get_player_by_class_id(20, 2), get_player_by_class_id(22, 4), random.Random("ditto-battles"), save_movie=True)
	# run_battle_with_trainers(get_player_by_class_id(22, 4), get_player_by_class_id(20, 2), random.Random("ditto-battles"), save_movie=True)

	#baton pass battles
	# run_battle_from_hashid("en153y37", save_movie=True)
	# run_battle_with_trainers(get_player_by_class_id(34, 2), get_player_by_class_id(59, 8), random.Random("baton-pass-battles"), save_movie=True)
	# for i in range(100):
	# 	print("Running battle!", i)
	# 	run_random_battle(save_movie=False)
	run_random_battle(save_movie=False)
	#
	# run_battle_from_hashid("e32d xd0-", save_movie=False)
	# run_battle_from_hashid("r1yj zw!g", save_movie=False)
	# run_battle_from_hashid("7w13 9w21", save_movie=False) #weirdly long battle

# run_random_battle(save_movie=False)
# test_battles_with_all_trainers()
