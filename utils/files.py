import os
import struct
import uuid
import zlib
from typing import Iterable

from constants import memory
from constants.file_paths import OUT_DIR
from constants.memory import MemoryAddress
from protobuf.battle_pb2 import BattleBatch
from utils.besssave import BessSave
from utils.data import reverse_characters


def name_to_bytes(name: str, length: int = memory.NAME_LENGTH) -> Iterable[int]:
	return (reverse_characters[name[i]] if i < len(name) else memory.NAME_TERMINATOR for i in range(length))


def get_stat(stat: bytearray) -> int:
	return stat[0] << 8 | stat[1]


def write_file(file: str, save: BessSave | bytearray) -> None:
	with open(file, 'wb') as f:
		if type(save) == BessSave:
			f.write(save.save)
		else:
			f.write(save)


def load_save(file: str) -> BessSave:
	with open(file, 'rb') as f:
		save = bytearray(f.read())
	return BessSave(save)


def get_current_pokemon_index(battle_save: BessSave):
	current_pokemon_index = battle_save.get_value(memory.wPartyMenuCursor)[0]
	# wPartyMenu cursor starts unpopulated (0), but is 1-indexed
	current_pokemon_index = max(current_pokemon_index, 1) - 1
	return current_pokemon_index


def save_battle_batch(batch: BattleBatch, batch_identifier: str, compressed=True) -> str:
	output_dir = os.path.abspath(f"{OUT_DIR}/batches/{batch_identifier}")
	os.makedirs(output_dir, exist_ok=True)
	batch_uuid = uuid.uuid4()
	batch_file = f"{output_dir}/{batch_uuid}.bin"
	if compressed:
		batch_file += '.gz'
	with open(batch_file, 'wb') as f:
		if not compressed:
			f.write(batch.SerializeToString())
		else:
			f.write(zlib.compress(batch.SerializeToString()))

	return batch_file


def load_battle_batch(path: str) -> BattleBatch:
	with open(path, 'rb') as f:
		batch = BattleBatch()
		file_data = f.read()
		if path.endswith('.gz'):
			file_data = zlib.decompress(file_data)
		batch.ParseFromString(file_data)
		return batch
