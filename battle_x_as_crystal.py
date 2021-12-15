import os
import random
import shutil

import constants.file_paths as files
from utils.bgb import call_bgb
from utils.data import *
from utils.demos import *
from utils.files import *
from utils.movies import build_movie, MovieContext


def load_trainer_info(trainer_class: int, trainer_id: int, in_save: bytearray, working_save: str) -> bytearray:
	save = in_save.copy()
	set_value(save, [trainer_class], memory.wOtherTrainerClass)
	set_value(save, [trainer_id], memory.wOtherTrainerID)
	write_file(working_save, save)

	call_bgb(in_save=working_save,
	         out_save=working_save,
	         breakpoint_list=['PlaceCommandCharacter'])

	return load_save(working_save)


def set_up_battle_save(base_save: bytearray, player_trainer_info: bytearray, enemy_class: int,
                       enemy_index: int) -> bytearray:
	battle_save = base_save.copy()

	copy_values(player_trainer_info, memory.wOTParty, battle_save, memory.wPlayerParty)

	enemy_party_size = get_value(player_trainer_info, memory.wOTPartyCount)[0]

	for i in range(enemy_party_size):
		pokemon = get_value(player_trainer_info, memory.enemyParty[i])
		pokemon_index = pokemon[0] - 1
		pokemon_name = name_to_bytes(pokemon_names[str(pokemon_index)])
		set_value(battle_save, pokemon_name, memory.playerPartyNicks[i])
		copy_values(player_trainer_info, memory.wStringBuffer1, battle_save, memory.playerPartyOTs[i])

	copy_values(player_trainer_info, memory.wStringBuffer1, battle_save, memory.wPlayerName)
	set_value(battle_save, [memory.NAME_TERMINATOR], memory.playerNameEnd)
	set_value(battle_save, [0x1], memory.wPlayerGender)  # TODO: Set gender properly

	set_value(battle_save, [enemy_class], memory.wOtherTrainerClass)
	set_value(battle_save, [enemy_index], memory.wOtherTrainerID)

	return battle_save


def get_ai_action(battle_save: bytearray, base_save: str, working_save: str, out_save: str):
	ai_save = load_save(base_save)
	swap_pairings(battle_save, ai_save)

	# TODO: wTrainerClass or whatever it is
	# TODO: Randomize rdiv w/ seeded value
	# TODO: Item counts
	# TODO: we may need to update more values here. Check the disassembly.

	# These allow us to make the game think our Pokemon is always on the last turn of Perish Song
	# set_value(ai_save, wEnemySubStatus1[0], [0x10], 1)
	# set_value(ai_save, wEnemyPerishCount[0], [0x1], 1)

	write_file(working_save, ai_save)

	# Open the AI state, wait for the results
	call_bgb(in_save=working_save, out_save=out_save, breakpoint_list=[
		# for switching:
		'LoadEnemyMon',
		# for move selection:
		'PlayerTurn_EndOpponentProtectEndureDestinyBond', 'EnemyTurn_EndOpponentProtectEndureDestinyBond',
		'AI_Switch',
		'EnemyUsedFullHeal', 'EnemyUsedMaxPotion', 'EnemyUsedFullRestore', 'EnemyUsedPotion', 'EnemyUsedSuperPotion',
		'EnemyUsedHyperPotion', 'EnemyUsedXAccuracy', 'EnemyUsedGuardSpec', 'EnemyUsedDireHit', 'EnemyUsedXAttack',
		'EnemyUsedXDefend', 'EnemyUsedXSpeed', 'EnemyUsedXSpecial',
	], demo=files.AI_DEMO)

	# Parse AI actions
	ai_output = load_save(out_save)
	return ai_output


def swap_pairings(source_save, target_save):
	# Copy data from battle save to ai save, swapping the player and enemy data

	for pairing in memory.player_enemy_pairs:
		player_address = pairing[0]
		enemy_address = pairing[1]

		copy_values(source_save, player_address, target_save, enemy_address)
		copy_values(source_save, enemy_address, target_save, player_address)


def initial_testing():
	# Set up working directory
	run_identifier = random.randint(1, 10000000)
	working_dir = os.path.abspath(f"./working/{run_identifier}")
	output_dir = os.path.abspath(f"./output/{run_identifier}")
	movie_working_dir = f"{working_dir}/movie"
	save_working_dir = f"{working_dir}/saves"
	demo_working_dir = f"{working_dir}/demo"
	movie_context = MovieContext(movie_name=str(run_identifier),
	                             movie_index=0,
	                             movie_working_dir=movie_working_dir,
	                             movie_output_dir=output_dir)

	for directory in [working_dir, output_dir, save_working_dir, demo_working_dir, movie_working_dir]:
		os.makedirs(directory, exist_ok=True)

	out_save_path = f"{save_working_dir}/{files.OUT_SAVE}"
	ai_input_save_path = f"{save_working_dir}/{files.AI_INPUT_SAVE}"
	ai_output_save_path = f"{save_working_dir}/{files.AI_OUTPUT_SAVE}"
	battle_save_path = f"{save_working_dir}/{files.BATTLE_SAVE}"
	out_demo_path = f"{demo_working_dir}/{files.OUT_DEMO}"

	print(files.BASE_DIR)
	shutil.copyfile(files.ROM_IMAGE, f"{save_working_dir}/{files.ROM_NAME}")
	shutil.copyfile(files.MEMORY_MAP, f"{save_working_dir}/{files.MEMORY_MAP_NAME}")

	# Randomly choose a player and enemy trainer
	seed = random.randint(0, 1000000000)
	print("seed", seed)
	random.seed(seed)
	player_trainer, enemy_trainer = random.choice(raw_trainer_data), random.choice(raw_trainer_data)

	player_class = player_trainer['class']
	player_index = player_trainer['instance']
	enemy_class = enemy_trainer['class']
	enemy_index = enemy_trainer['instance']

	# player_class = 63
	# player_index = 1
	# enemy_class = 16
	# enemy_index = 1

	print(f"You are {get_trainer_identifier(player_trainer)}. Your opponent is {get_trainer_identifier(enemy_trainer)}")

	# Load the data for the player trainer
	base_save = load_save(files.BASE_SAVE)

	player_trainer_info = load_trainer_info(player_class, player_index, base_save, out_save_path)

	# Set up the initial battle state
	battle_save = set_up_battle_save(base_save, player_trainer_info, enemy_class, enemy_index)

	write_file(battle_save_path, battle_save)
	write_file(out_demo_path, generate_demo([]))

	while True:
		# Play until we reach a menu or win/lose
		total_clocks = get_total_clocks(battle_save)
		breakpoint_condition = f"TOTALCLKS!=${total_clocks:x}"
		call_bgb(in_save=battle_save_path, out_save=battle_save_path, breakpoint_list=[
			f'BattleMenu/{breakpoint_condition}',
			f'SetUpBattlePartyMenu/{breakpoint_condition}',
			f'WinTrainerBattle/{breakpoint_condition}',
			f'LostBattle/{breakpoint_condition},',
		], demo=out_demo_path, movie_context=movie_context)

		battle_save = load_save(battle_save_path)

		pc = get_program_counter(battle_save)
		print(f'Program counter: {pc:x}')

		# Which breakpoint did we hit?
		if pc == memory.breakpoints["WinTrainerBattle"]:
			# Player won!

			print("You win!")
			break
		elif pc == memory.breakpoints["LostBattle"]:
			# Enemy won!

			print("You lose!")
			break
		elif pc == memory.breakpoints["SetUpBattlePartyMenu"]:
			# AI is forced to switch out, what should we switch to?

			ai_output = get_ai_action(battle_save=battle_save,
			                          base_save=files.BASE_SWITCH_SAVE,
			                          working_save=ai_input_save_path,
			                          out_save=ai_output_save_path)

			selected_pokemon_index = get_value(ai_output, memory.wCurPartyMon)[0]
			current_pokemon_index = get_value(battle_save, memory.wPartyMenuCursor)[0]

			# wPartyMenu cursor starts unpopulated (0), but is 1-indexed
			current_pokemon_index = max(current_pokemon_index, 1) - 1
			print("The selected pokemon was", selected_pokemon_index, "and the current pokemon was",
			      current_pokemon_index)

			button_sequence = choose_pokemon(current_pokemon_index, selected_pokemon_index)
		else:
			# We're at the battle menu, what should we choose?

			ai_output = get_ai_action(battle_save=battle_save,
			                          base_save=files.BASE_AI_SAVE,
			                          working_save=ai_input_save_path,
			                          out_save=ai_output_save_path)

			ai_pc = get_program_counter(ai_output)

			if ai_pc == memory.breakpoints["AI_Switch"]:
				print("The AI wants to switcharino")
				target_pokemon = get_value(ai_output, memory.wEnemySwitchMonIndex)[0] - 1
				current_pokemon_index = get_value(battle_save, memory.wPartyMenuCursor)[0]

				# wPartyMenu cursor starts unpopulated (0), but is 1-indexed
				current_pokemon_index = max(current_pokemon_index, 1) - 1
				print("The selected pokemon was", target_pokemon, "and the current pokemon was",
				      current_pokemon_index)

				button_sequence = select_switch() + choose_pokemon(current_pokemon_index, target_pokemon)

			else:
				selected_move_index = get_value(ai_output, memory.wCurEnemyMoveNum)[0]
				print("The selected move was", selected_move_index)
				current_move_index = get_value(battle_save, memory.wCurMoveNum)[0]

				button_sequence = select_move(current_move_index, selected_move_index)

		write_file(out_demo_path, button_sequence)

	build_movie(movie_context)


if __name__ == '__main__':
	initial_testing()
