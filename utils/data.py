import json
from typing import Tuple


def load_json(path: str) -> dict:
	with open(path, 'r', encoding='utf-8') as f:
		return json.load(f)


def load_memory_map(path: str) -> Tuple[dict, dict]:
	base = load_json(path)
	return {int(key, 16): value for key, value in base.items()}, {value: int(key, 16) for key, value in base.items()}


def load_one_way_memory_map(path: str) -> dict:
	base = load_json(path)
	return {int(key, 16): value for key, value in base.items()}


def get_trainer_identifier(trainer_dict):
	return f"{trainer_dict['title']} {trainer_dict['name']} #{trainer_dict['rematch']} (class: {trainer_dict['class']}, id: {trainer_dict['instance']})"


pokemon_names = load_json("data_files/pokemon_names.json")
raw_trainer_data = load_json("data_files/trainers.json")
characters, reverse_characters = load_memory_map('data_files/charmap.json')
moves = load_one_way_memory_map('data_files/moves.json')


def get_player_by_trainer_index(trainer_index: int) -> dict:
	return raw_trainer_data[trainer_index]


def get_trainer_index(class_id: int, instance_id: int) -> int:
	for i, trainer in enumerate(raw_trainer_data):
		if trainer['class'] == class_id and trainer['instance'] == instance_id:
			return i
	else:
		raise ValueError(f"No trainer found with class_id {class_id} and instance_id {instance_id}")


def get_player_by_class_id(class_id: int, instance_id: int) -> dict:
	return get_player_by_trainer_index(get_trainer_index(class_id, instance_id))
