import json
from typing import Tuple


def load_json(path: str) -> dict:
	with open(path, 'r', encoding='utf-8') as f:
		return json.load(f)


def load_memory_map(path: str) -> Tuple[dict, dict]:
	base = load_json(path)
	return {int(key, 16): value for key, value in base.items()}, {value: int(key, 16) for key, value in base.items()}


def get_trainer_identifier(trainer_dict):
	return f"{trainer_dict['title']} {trainer_dict['name']} #{trainer_dict['rematch']} (class: {trainer_dict['class']}, id: {trainer_dict['instance']})"

pokemon_names = load_json("data_files/pokemon_names.json")
raw_trainer_data = load_json("data_files/trainers.json")
characters, reverse_characters = load_memory_map('data_files/charmap.json')