import os.path
import pickle
import random
import shutil
import sys
import time
import zlib
from typing import List, Dict, Tuple, Literal

from rich.pretty import pprint

from analysis_models.trainer import Trainer, Battle, Pokémon
from battle_x_as_crystal import run_battle_from_hashid
from protobuf.battle_pb2 import BattleSummary
from protobuf.game_data_pb2 import MoveIdentifier
from utils.battle_printer import print_battle_log
from utils.data import get_player_by_class_id
from utils.files import load_battle_batch

import numpy as np
from sklearn import linear_model


def turn_counts(raw_battles):
	turn_counts = [len(b.turns) for b in raw_battles]

	most_turns = max(turn_counts)

	print("number of turns\tnumber of battles")
	for i in range(1, most_turns + 1):
		print(f"{i}\t{turn_counts.count(i)}")


def player_enemy_balance(raw_battles):
	player_wins = len([b for b in raw_battles if b.winner == BattleSummary.Winner.PLAYER])
	enemy_wins = len([b for b in raw_battles if b.winner == BattleSummary.Winner.ENEMY])

	assert player_wins + enemy_wins == len(raw_battles)

	print("player wins", player_wins, player_wins / (player_wins + enemy_wins))
	print("enemy wins", enemy_wins, enemy_wins / (player_wins + enemy_wins))


def print_longest_battle(raw_battles):
	longest_battle = max(raw_battles, key=lambda b: len(b.turns))
	print_battle_log(longest_battle)


def trainer_to_tuple(trainer: BattleSummary.TrainerID) -> tuple:
	return trainer.trainer_class, trainer.instance


def trainer_tuple_to_name(trainer: tuple) -> str:
	trainer_dict = get_player_by_class_id(*trainer)
	return f"{trainer_dict['title']} {trainer_dict['name']} #{trainer_dict['rematch']}"


def trainer_id_to_name(trainer: BattleSummary.TrainerID) -> str:
	return trainer_tuple_to_name(trainer_to_tuple(trainer))


def calc_wl(raw_battles: List[BattleSummary]):
	trainers = {}
	for battle in raw_battles:
		trainers[trainer_to_tuple(battle.player)] = 0

	for battle in raw_battles:
		if battle.winner == BattleSummary.Winner.PLAYER:
			trainers[trainer_to_tuple(battle.player)] += 1
		else:
			trainers[trainer_to_tuple(battle.enemy)] += 1
	trainer_list = list(trainers.keys())
	trainer_list.sort(key=lambda t: trainers[t])
	# for trainer in trainer_list:
	# 	print(f"{trainer_tuple_to_name(trainer) : <25}\t{trainers[trainer] : >4}\t{trainer}")

	return trainers


def find_wins_by_trainer(raw_battles: List[BattleSummary], trainer: tuple):
	trainer_wins = [b for b in raw_battles if (
			b.winner == BattleSummary.Winner.PLAYER and trainer_to_tuple(b.player) == trainer or
			b.winner == BattleSummary.Winner.ENEMY and trainer_to_tuple(b.enemy) == trainer
	)]

	for win in trainer_wins:
		print_battle_log(win)


def find_most_used_moves(raw_battles: List[BattleSummary]):
	moves = {}
	for move in MoveIdentifier.values():
		moves[move] = 0
	for battle in raw_battles:
		for turn in battle.turns:
			if turn.selected_move:
				moves[turn.selected_move] += 1

	moves_list = list(moves.keys())
	moves_list.sort(key=lambda m: moves[m], reverse=True)
	for move in moves_list:
		print(f"{MoveIdentifier.Name(move) : <25}\t{moves[move] : >4}")


def find_red_should_snore(raw_battles: List[BattleSummary]):
	for battle in raw_battles:
		if battle.player == BattleSummary.TrainerID(trainer_class=63, instance=1):
			for turn in battle.turns:
				if turn.selected_move == MoveIdentifier.REST:
					print_battle_log(battle)
					print()
					print("-----------------------------------------------------")
					print()
					break


def calculate_trainer_elo(raw_battles: List[BattleSummary]):
	trainers = set()
	for battle in raw_battles:
		trainers.add(trainer_to_tuple(battle.player))
		trainers.add(trainer_to_tuple(battle.enemy))

	trainers = list(trainers)
	N = len(trainers)
	X = []
	Y = []
	for battle in raw_battles:
		if trainer_to_tuple(battle.player) != trainer_to_tuple(battle.enemy):
			t1 = trainers.index(trainer_to_tuple(battle.player))
			t2 = trainers.index(trainer_to_tuple(battle.enemy))
			v = np.zeros(N)
			v[t1] = 1
			v[t2] = -1
			X.append(v)
			Y.append(battle.winner == BattleSummary.Winner.PLAYER)

	clf = linear_model.LogisticRegression(max_iter=1000)
	clf.fit(X, Y)

	elo_results = list(clf.coef_[0] * 173 + 1500)

	elo_trainers = {}
	for trainer in trainers:
		elo_trainers[trainer] = elo_results[trainers.index(trainer)]
	return elo_trainers, clf.intercept_[0]


def calculate_elo_badly(raw_battles):
	trainers = set()
	for battle in raw_battles:
		trainers.add(trainer_to_tuple(battle.player))
		trainers.add(trainer_to_tuple(battle.enemy))

	trainers = {
		trainer: 1500 for trainer in trainers
	}

	shuffled_battles = [*raw_battles]
	random.shuffle(shuffled_battles)

	for battle in shuffled_battles:
		t1 = trainer_to_tuple(battle.player)
		t2 = trainer_to_tuple(battle.enemy)
		if t1 != t2:
			r1 = 10 ** (trainers[t1] / 400)
			r2 = 10 ** (trainers[t2] / 400)

			e1 = r1 / (r1 + r2)
			e2 = r2 / (r1 + r2)

			if battle.winner == BattleSummary.Winner.PLAYER:
				s1, s2 = 1, 0
			else:
				s1, s2 = 0, 1

			trainers[t1] += 20 * (s1 - e1)
			trainers[t2] += 20 * (s2 - e2)

	return trainers


def run_biggest_upsets(raw_battles, elo_trainers):
	for i, trainer in enumerate(list(elo_trainers.keys())[99:]):
		trainer_victories = [b for b in raw_battles if (
				trainer_to_tuple(b.player) == trainer and b.winner == BattleSummary.PLAYER or trainer_to_tuple(
			b.enemy) == trainer and b.winner == BattleSummary.ENEMY
		)]
		print(f"{i + 1}. {trainer_tuple_to_name(trainer)} {len(trainer_victories)} battles")
		biggest_upset = 0
		biggest_elo = -100000
		for battle in trainer_victories:
			if battle.winner == BattleSummary.Winner.PLAYER:
				elo = elo_trainers[trainer_to_tuple(battle.enemy)]
			else:
				elo = elo_trainers[trainer_to_tuple(battle.player)]
			if elo > biggest_elo:
				biggest_elo = elo
				biggest_upset = battle
		print(
			f"{biggest_upset.seed}\t{trainer_tuple_to_name(trainer_to_tuple(biggest_upset.player))} {trainer_tuple_to_name(trainer_to_tuple(biggest_upset.enemy))}")
		run_battle_from_hashid(biggest_upset.seed, save_movie=True)
		movie_path = f"w:/elo_world_output/crystal/{biggest_upset.seed}/movies/{biggest_upset.seed}.mov"
		try:
			shutil.copy(movie_path,
			            f"./validation_movies/{biggest_upset.seed} winner {trainer_tuple_to_name(trainer).replace('?', '')}.mov")
		except:
			print("oops!")


def build_pokemon(pokemon: List[dict]):
	return [Pokémon(
		level=p["level"],
		species=p["species"],
		moves=p["moves"] if "moves" in p else None,
		held_item=p["item"] if "item" in p else None,
	) for p in pokemon]


def build_trainer(player, trainers) -> Trainer:
	trainer_tuple = (player.trainer_class, player.instance)
	if trainer_tuple in trainers:
		return trainers[trainer_tuple]
	trainer_dict = get_player_by_class_id(*trainer_tuple)
	new_trainer = Trainer(
		class_id=player.trainer_class,
		instance_id=player.instance,
		class_name=trainer_dict["title"],
		name=trainer_dict["name"],
		rematch=trainer_dict["rematch"],
		dvs=trainer_dict["dvs"],
		gender=trainer_dict["gender"],
		strategy=trainer_dict["techniques"],
		pokémon=build_pokemon(trainer_dict["pokemon"]),
		items=trainer_dict["items"],
		switch_style=trainer_dict["switch_style"]
	)
	trainers[trainer_tuple] = new_trainer
	return new_trainer


def print_longest_battles(battle_list):
	battle_list.sort(key=lambda b: len(b.turns), reverse=True)
	for i, battle in enumerate(battle_list[:100]):
		print(
			f"#{i+1} {len(battle.turns)} turns: {battle.seed} {trainer_tuple_to_name(trainer_to_tuple(battle.player))} {trainer_tuple_to_name(trainer_to_tuple(battle.enemy))}")


def print_biggest_upsets(battle_list: List[Battle]):
	battle_list.sort(key=lambda b: b.losing_trainer.elo - b.winning_trainer.elo, reverse=True)
	for battle in battle_list[:100]:
		print(
			f"{int(battle.losing_trainer.elo - battle.winning_trainer.elo)} elo:\t{battle.seed} {battle.winning_trainer.full_name} {battle.losing_trainer.full_name}")


def print_trainer_biggest_upsets(trainerList: List[Trainer]):
	trainerList.sort(key=lambda t: t.elo)
	for trainer in trainerList:
		biggest_upset = max(trainer.victories, key=lambda b: b.losing_trainer.elo)
		biggest_defeat = min(trainer.defeats, key=lambda b: b.winning_trainer.elo)
		print(
			"\t".join((f"{trainer.class_id},{trainer.instance_id}", biggest_upset.seed, biggest_upset.losing_trainer.full_name, str(biggest_upset.losing_trainer.elo), biggest_defeat.seed, biggest_defeat.winning_trainer.full_name, str(biggest_defeat.winning_trainer.elo))))


def main():
	(battles, trainers, raw_battles) = load_data()
	trainer_list = list(trainers.values())
	battle_list = list(battles.values())

	print("all done here")

	print("longest battles:")
	print_longest_battles(raw_battles)

	print("biggest upsets:")
	print_biggest_upsets(battle_list)

	print("trainer biggest upsets:")
	print_trainer_biggest_upsets(trainer_list)

	print("battles won by player", len([b for b in battle_list if b.winner == "player"]))
	print("battles won by enemy", len([b for b in battle_list if b.winner != "player"]))



# print_tsv(trainer_list)


def print_tsv(trainer_list):
	print("\t".join([
		"class", "instance", "gender", "class_name", "name", "rematch", "later rematch",
		"avg. level", "pokemon", "custom moves", "held items", "DV total",
		"items", "strats", "switch style",
		"wins", "losses", "elo"
	]))
	for trainer in trainer_list:
		print("\t".join((str(prop) for prop in [
			trainer.class_id, trainer.instance_id, trainer.gender_symbol, trainer.class_name, trainer.name,
			trainer.rematch, trainer.has_later_rematch,
			trainer.average_level, ", ".join(p.species for p in trainer.pokémon), trainer.pokemon_have_moves,
			trainer.pokemon_have_items, trainer.dv_total,
			", ".join(trainer.items), ", ".join(trainer.strategy), trainer.switch_style,
			trainer.wins, trainer.losses, trainer.elo
		])))


def load_data():
	raw_battles = load_battle_batch("omega_batch.bin.gz").battles
	if os.path.exists("omega.pickle"):
		with open("omega.pickle", "rb") as f:
			return *pickle.loads(zlib.decompress(f.read())), raw_battles
	start = time.time()
	print("time taken", time.time() - start)
	trainers: Dict[Tuple[int, int], Trainer] = {}
	battles: Dict[str, Battle] = {}
	for battle in raw_battles:
		player = build_trainer(battle.player, trainers)
		enemy = build_trainer(battle.enemy, trainers)

		new_battle = Battle(seed=battle.seed, player=player, enemy=enemy,
		                    winner=("player" if battle.winner == BattleSummary.Winner.PLAYER else "enemy"),
		                    winning_trainer=player if battle.winner == BattleSummary.Winner.PLAYER else enemy,
		                    losing_trainer=enemy if battle.winner == BattleSummary.Winner.PLAYER else player
		                    )
		battles[battle.seed] = new_battle

		new_battle.player.battles.append(new_battle)
		if new_battle.player != new_battle.enemy:
			new_battle.enemy.battles.append(new_battle)

		new_battle.winning_trainer.wins += 1
		new_battle.winning_trainer.victories.append(new_battle)

		new_battle.losing_trainer.losses += 1
		new_battle.losing_trainer.defeats.append(new_battle)
	print(len(battles))
	print(len(trainers))
	elo_trainers, elo_hfa = calculate_trainer_elo(raw_battles)
	print("home field advantage", elo_hfa)
	for trainer in elo_trainers.keys():
		trainers[trainer].elo = elo_trainers[trainer]
	print("saving pickle")
	trainer_list = list(trainers.values())
	for trainer in trainer_list:
		if any(t.class_name == trainer.class_name and t.name == trainer.name and t.rematch > trainer.rematch for t in
		       trainer_list):
			trainer.has_later_rematch = True
	sys.setrecursionlimit(1000000)
	with open('omega.pickle', 'wb') as f:
		f.write(zlib.compress(
			pickle.dumps((battles, trainers), protocol=pickle.HIGHEST_PROTOCOL),
			level=9)
		)
	return battles, trainers, raw_battles


# trainer_wl = calc_wl(raw_battles)
#
# elo_trainers, elo_hfa = calculate_trainer_elo(raw_battles)
# print("home field advantage", elo_hfa)
#
# elo_trainer_list = list(elo_trainers.keys())
# elo_trainer_list.sort(key=lambda t: elo_trainers[t])
#
# for i, trainer in enumerate(elo_trainer_list):
# 	print(
# 		f"{trainer_tuple_to_name(trainer) : <25}\t{elo_trainers[trainer] : >10.2f}\t{trainer_wl[trainer]}\t{trainer}")
#
# run_biggest_upsets(raw_battles, elo_trainers)


# bad_elo_trainers = calculate_elo_badly(raw_battles)
# bad_elo_trainer_list = list(bad_elo_trainers.keys())
# bad_elo_trainer_list.sort(key=lambda t: bad_elo_trainers[t])
#
# for i, trainer in enumerate(bad_elo_trainer_list):
# 	print(f"{trainer_tuple_to_name(trainer) : <25}\t{bad_elo_trainers[trainer] : >10.2f}\t{trainer_wl[trainer]}\t{trainer}")


# print(len(raw_battles))
# turn_counts(raw_battles)
# player_enemy_balance(raw_battles)
# print_longest_battle(raw_battles)
# calc_wl(raw_battles)
# find_wins_by_trainer(raw_battles, (36, 1))
# find_most_used_moves(raw_battles)


# find_red_should_snore(raw_battles)

if __name__ == '__main__':
	main()
