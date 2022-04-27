from typing import Tuple, List

from protobuf.battle_pb2 import *
from utils.battle_printer import print_battle_summary, print_turn_summary, print_battle_winner


def start_new_battle(seed: str, player: Tuple[int, int], enemy: Tuple[int, int]) -> BattleSummary:
	battle = BattleSummary()

	battle.seed = seed

	battle.player.trainer_class = player[0]
	battle.player.instance = player[1]

	battle.enemy.trainer_class = enemy[0]
	battle.enemy.instance = enemy[1]

	print_battle_summary(battle)

	return battle

def add_turn(battle: BattleSummary, selected_action: str, action_outcome: int, player_battle_mon: Tuple[int, int, int, int], enemy_battle_mon: Tuple[int, int, int, int]) -> None:
	new_turn = BattleSummary.TurnDescriptor()
	new_turn.turn_number = len(battle.turns)

	match selected_action:
		case 'MOVE':
			new_turn.selected_action = BattleSummary.TurnDescriptor.Action.MOVE
			new_turn.selected_move = action_outcome
		case 'SWITCH':
			new_turn.selected_action = BattleSummary.TurnDescriptor.Action.SWITCH
			new_turn.selected_pokemon = action_outcome
		case 'ITEM':
			new_turn.selected_action = BattleSummary.TurnDescriptor.Action.ITEM
			new_turn.selected_item = action_outcome
		case 'FORCE_SWITCH':
			new_turn.selected_action = BattleSummary.TurnDescriptor.Action.FORCE_SWITCH
			new_turn.selected_pokemon = action_outcome

	new_turn.player_mon.species = player_battle_mon[0]
	new_turn.player_mon.hp = player_battle_mon[1]
	new_turn.player_mon.max_hp = player_battle_mon[2]
	new_turn.player_mon.party_index = player_battle_mon[3]

	new_turn.enemy_mon.species = enemy_battle_mon[0]
	new_turn.enemy_mon.hp = enemy_battle_mon[1]
	new_turn.enemy_mon.max_hp = enemy_battle_mon[2]
	new_turn.enemy_mon.party_index = enemy_battle_mon[3]

	battle.turns.append(new_turn)

	print_turn_summary(battle, new_turn.turn_number)

def end_battle(battle: BattleSummary, winner: str):
	match winner:
		case 'PLAYER':
			battle.winner = BattleSummary.Winner.PLAYER
		case 'ENEMY':
			battle.winner = BattleSummary.Winner.ENEMY
		case 'TURN_LIMIT':
			battle.winner = BattleSummary.Winner.DRAW_BY_TURN_COUNT
		case 'EXCEPTION':
			battle.winner = BattleSummary.Winner.DRAW_BY_EXCEPTION

	print_battle_winner(battle)


def make_batch(battles: List[BattleSummary]) -> BattleBatch:
	batch = BattleBatch()
	batch.battles.extend(battles)
	return batch