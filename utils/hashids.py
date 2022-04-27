from hashids import Hashids

import utils.data
from utils.data import get_trainer_index, get_player_by_trainer_index

SAFE_ALPHABET = "abcdefghijkmnopqrstuvwxyz1234567890-!"
SALT = "crystal"

hash_encoder = Hashids(salt=SALT, alphabet=SAFE_ALPHABET, min_length=8)

trainer_count = len(utils.data.raw_trainer_data)


def encode_battle(player_class: int, player_instance: int, enemy_class: int, enemy_instance: int, battle_nonce: int) -> str:
	player_instance = get_trainer_index(player_class, player_instance)
	enemy_instance = get_trainer_index(enemy_class, enemy_instance)

	battle_index = player_instance + (enemy_instance * trainer_count) + ((battle_nonce + 1) * trainer_count ** 2)

	return hash_encoder.encode(battle_index)


def decode_battle(battle_id: str) -> (dict, dict, int):
	battle_id = battle_id.replace(" ", "")
	battle_index = hash_encoder.decode(battle_id)[0]

	player_index = battle_index % trainer_count
	battle_index = battle_index // trainer_count
	enemy_index = battle_index % trainer_count
	battle_nonce = (battle_index // trainer_count) - 1

	return get_player_by_trainer_index(player_index), get_player_by_trainer_index(enemy_index), battle_nonce


def prettify_hashid(hashid: str) -> str:
	return hashid[0:4] + " " + hashid[4:]
