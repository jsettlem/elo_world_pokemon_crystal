import collections
import itertools
from pprint import pprint

from protobuf.battle_pb2 import BattleSummary
from protobuf.game_data_pb2 import PokemonSpecies
from utils.battle_printer import print_battle_log
from utils.files import load_battle_batch


def main():
	# sample_batch = "W:/elo_world_output/crystal/batches/command_server/30ab01bb-581a-4dcf-89e3-92e2611e0b69.bin.gz"
	sample_batch = "showdown_omega_batch_4.bin/c2dd3c15-0f5c-4064-9f68-3cf662af6940.bin"
	battles = load_battle_batch(sample_batch)


	# print(" ".join(str(len(battle.turns)) for battle in battles.battles))

	deaths = [len([turn for turn in battle.turns if turn.selected_action == BattleSummary.TurnDescriptor.Action.FORCE_SWITCH]) for battle in battles.battles]
	pprint(collections.Counter(deaths))
	turn_counts = [len(battle.turns) for battle in battles.battles]
	pprint(collections.Counter(turn_counts))
	print(max(turn_counts))
	second_turn_switches = len([battle for battle in battles.battles if len(battle.turns) > 1 and battle.turns[1].selected_action == BattleSummary.TurnDescriptor.Action.FORCE_SWITCH])
	print(second_turn_switches / len(battles.battles))
	print("total turn count", sum(turn_counts))
	all_enemy_mons = [PokemonSpecies.Name(turn.enemy_mon.species - 1) for battle in battles.battles for turn in battle.turns]
	pprint(collections.Counter(all_enemy_mons))

	venusaur_battles = [battle for battle in battles.battles if any(turn.enemy_mon.species == 3 for turn in battle.turns)]

	print("number of venusaur battles", len(venusaur_battles))

	for battle in battles.battles:
		if len(battle.turns) > 30:
			print("long battle", battle.seed, len(battle.turns))

			if any(turn.enemy_mon.species == 3 for turn in battle.turns):
				print("venusaur battle", battle.seed, len(battle.turns))
		if battle.winner != BattleSummary.ENEMY:
			print("not as expected")
		# if len([turn for turn in battle.turns if turn.selected_action == BattleSummary.TurnDescriptor.Action.FORCE_SWITCH]) != 5:
		# 	print("weird turns", battle.seed)
		# 	print_battle_log(battle)


if __name__ == '__main__':
	main()