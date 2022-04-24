import random

from rich.console import Console, RenderableType, Group
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree

from protobuf import game_data_pb2
from protobuf.battle_pb2 import BattleSummary
from protobuf.game_data_pb2 import MoveIdentifier, ItemIdentifier, PokemonSpecies
from utils.data import get_player_by_class_id

import colorsys

console = Console(color_system="truecolor", width=120)


def create_panel(renderable: RenderableType, battle_id: str, subtitle: str) -> Panel:
	return Panel(
		renderable,
		title=f"Battle [b u on black]{battle_id}",
		subtitle=subtitle,
		style="on grey7",
		border_style=get_style_from_seed(battle_id),
		safe_box=False
	)


def get_style_from_seed(seed: str) -> str:
	color_rng = random.Random(seed)
	bg_hue = color_rng.random()
	fg_hue = color_rng.random()
	bg_color = colorsys.hsv_to_rgb(bg_hue, 1.0, 0.2)
	fg_color = colorsys.hsv_to_rgb(fg_hue, 1.0, 0.9)
	color_to_string = lambda c: "rgb(" + ','.join(str(int(b * 255)) for b in c) + ")"
	return f"{color_to_string(fg_color)} on {color_to_string(bg_color)}"


def get_trainer_name(trainer: dict) -> str:
	gender_indicators = {
		"MALE": "[bright_cyan]♂[/]",
		"FEMALE": "[bright_magenta]♀[/]",
		"ENBY": "[bright_yellow]⚥[/]"
	}
	return f"{gender_indicators[trainer['gender']]}[b]{trainer['title']}[/b] {trainer['name']} [grey50]#{trainer['rematch']}[/] [grey30](class {trainer['class']}, instance {trainer['instance']})"


def get_pokemon_tree(pokemon: dict) -> Tree:
	pokemon_tree = Tree(f"[grey50]Lv. [b]{pokemon['level']:>2}[/][/] {pokemon['species']}",
	                    guide_style="grey27")
	if "item" in pokemon:
		pokemon_tree.add(f"[grey46]{pokemon['item']}")
	else:
		pokemon_tree.add("[dark_red]No item")
	if "moves" in pokemon:
		pokemon_tree.add("[grey46]" + ",".join(move for move in pokemon["moves"] if move))

	else:
		pokemon_tree.add("Standard moves")

	return pokemon_tree


def get_trainer_tree(trainer: dict) -> Tree:
	trainer_tree = Tree(get_trainer_name(trainer))
	if trainer["items"]:
		trainer_tree.add("[grey70]" + ", ".join(item for item in trainer["items"] if item))
	else:
		trainer_tree.add("[dark_red]No items")
	pokemon_tree = trainer_tree.add("[cornsilk1]Pokémon")
	for pokemon in trainer["pokemon"]:
		pokemon_tree.add(get_pokemon_tree(pokemon))
	return trainer_tree


def print_battle_summary(battle: BattleSummary):
	battle_id = battle.seed
	player = get_player_by_class_id(battle.player.trainer_class, battle.player.instance)
	enemy = get_player_by_class_id(battle.enemy.trainer_class, battle.enemy.instance)

	player_tree = get_trainer_tree(player)
	enemy_tree = get_trainer_tree(enemy)

	summary_columns = Columns([player_tree, enemy_tree], )

	console.print(create_panel(summary_columns, battle_id, "Battle summary"))


def get_switch_mon(mon_index: int, battle: BattleSummary) -> str:
	player = get_player_by_class_id(battle.player.trainer_class, battle.player.instance)

	switch_mon = player["pokemon"][mon_index]["species"]

	return f"[i grey50]#{mon_index + 1}[/] [b u]{switch_mon}[/]"


def print_turn_summary(battle: BattleSummary, turn_number: int):
	battle_id = battle.seed
	turn = battle.turns[turn_number]

	match turn.selected_action:
		case BattleSummary.TurnDescriptor.Action.MOVE:
			action_summary = f"Player used [bright_white on red]move[/] [b u]{MoveIdentifier.Name(turn.selected_move)}"
		case BattleSummary.TurnDescriptor.Action.ITEM:
			action_summary = f"Player used [bright_white on yellow]item[/] [b u]{ItemIdentifier.Name(turn.selected_item)}"
		case BattleSummary.TurnDescriptor.Action.SWITCH:
			action_summary = f"Player [bright_white on green]switched[/] to {get_switch_mon(turn.selected_pokemon, battle)}"
		case BattleSummary.TurnDescriptor.Action.FORCE_SWITCH:
			action_summary = f"Player [bright_white on grey15]force switched[/] to {get_switch_mon(turn.selected_pokemon, battle)}"
		case _:
			action_summary = ""

	battle_mon_summary = get_battle_mon_summary(battle, turn_number)

	turn_summary = Group(
		action_summary,
		battle_mon_summary
	)

	console.print(create_panel(turn_summary, battle_id, f"Turn [b]{turn_number}"))


def get_battle_mon_summary(battle: BattleSummary, turn_number: int) -> RenderableType:
	turn = battle.turns[turn_number]
	player_mon = turn.player_mon
	enemy_mon = turn.enemy_mon

	player = get_player_by_class_id(battle.player.trainer_class, battle.player.instance)
	enemy = get_player_by_class_id(battle.enemy.trainer_class, battle.enemy.instance)

	player_party_count = len(player["pokemon"])
	enemy_party_count = len(enemy["pokemon"])
	mon_panel = Columns([
		get_mon_summary(player_mon, player_party_count),
		get_mon_summary(enemy_mon, enemy_party_count)
	])
	return mon_panel


def get_mon_summary(mon: BattleSummary.TurnDescriptor.BattleMon, party_count: int) -> RenderableType:
	party_balls = ""
	for i in range(6):
		if i >= party_count:
			party_balls += "[grey11]◓[/]"
		elif i == mon.party_index:
			party_balls += "[bright_red]◓[/]"
		else:
			party_balls += "[dark_red]◓[/]"

	mon_name = f"{party_balls} [i grey50]#{mon.party_index + 1}[/] [b]{PokemonSpecies.Name(mon.species - 1)}[/] - [grey50]{mon.hp} / {mon.max_hp} "

	health_percent = mon.hp / mon.max_hp
	if health_percent > 0.3:
		health_color = "green"
	elif health_percent > 0.1:
		health_color = "yellow"
	else:
		health_color = "red"
	health_bar_width = 30
	health_bar = f"[bright_{health_color}]{'█' * int(health_percent * health_bar_width)}[/][grey11]{'█' * int((1 - health_percent) * health_bar_width)}[/] "

	return Group(
		mon_name,
		health_bar
	)
