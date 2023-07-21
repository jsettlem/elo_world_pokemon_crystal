import collections
import itertools
from pprint import pprint

from protobuf.battle_pb2 import BattleSummary
from protobuf.game_data_pb2 import PokemonSpecies, MoveIdentifier, BATON_PASS
from utils.battle_printer import print_battle_log
from utils.files import load_battle_batch


def main():
	# sample_batch = "W:/elo_world_output/crystal/batches/command_server/30ab01bb-581a-4dcf-89e3-92e2611e0b69.bin.gz"
	sample_batch = "showdown_omega_batch_5.bin/42c4a84f-f70d-4e59-a822-9f3611c30421.bin"
	battles = load_battle_batch(sample_batch)


	print("number of battles", len(battles.battles))



	# print(" ".join(str(len(battle.turns)) for battle in battles.battles))

	deaths = [len([turn for turn in battle.turns if turn.selected_action == BattleSummary.TurnDescriptor.Action.FORCE_SWITCH]) for battle in battles.battles]
	print("deaths")
	pprint(collections.Counter(deaths))
	turn_counts = [len(battle.turns) for battle in battles.battles]
	print("turns")
	pprint(collections.Counter(turn_counts))
	print(max(turn_counts))
	min_turns = min(turn_counts)
	print(min_turns)
	# second_turn_switches = len([battle for battle in battles.battles if len(battle.turns) > 1 and battle.turns[1].selected_action == BattleSummary.TurnDescriptor.Action.FORCE_SWITCH])
	# print(second_turn_switches / len(battles.battles))


	# print("turn counts")
	# print(sum(turn_counts))
	# all_enemy_mons = [PokemonSpecies.Name(turn.enemy_mon.species - 1) for battle in battles.battles for turn in battle.turns]
	# print("enemy mons")
	# pprint(collections.Counter(all_enemy_mons))


	# venusaur_battles = [battle for battle in battles.battles if any(turn.enemy_mon.species == 3 for turn in battle.turns)]

	# print("number of venusaur battles", len(venusaur_battles))

	for battle in battles.battles:

		if len(battle.turns) > 30:
			print("long battle", battle.seed, len(battle.turns))

			if any(turn.enemy_mon.species == 3 for turn in battle.turns):
				print("venusaur battle", battle.seed, len(battle.turns))
		if (len(battle.turns) < 15) and battle.enemy.trainer_class != 64:
			print("short battle", battle.seed, len(battle.turns))
		if battle.winner == BattleSummary.ENEMY and battle.enemy.trainer_class != 63 or battle.winner == BattleSummary.PLAYER and battle.player.trainer_class != 63:
			print("not as expected")
		# if len([turn for turn in battle.turns if turn.selected_action == BattleSummary.TurnDescriptor.Action.FORCE_SWITCH]) != 5:
		# 	print("weird turns", battle.seed)
		# 	print_battle_log(battle)
		if (battle.turns[0].selected_action == BattleSummary.TurnDescriptor.Action.SWITCH) and battle.player.trainer_class == 64:
			print("switched first turn", battle.seed)

	# print("number of battles with venusaur", len(venusaur_battles


if __name__ == '__main__':
	main()
