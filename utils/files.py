import os
import struct
import uuid
import zlib
from typing import Iterable

from constants import memory
from constants.file_paths import OUT_DIR
from constants.memory import MemoryAddress
from protobuf.battle_pb2 import BattleBatch
from utils.data import reverse_characters


def name_to_bytes(name: str, length: int = memory.NAME_LENGTH) -> Iterable[int]:
	return (reverse_characters[name[i]] if i < len(name) else memory.NAME_TERMINATOR for i in range(length))


def get_value(source: bytearray, address: "MemoryAddress") -> bytearray:
	offset = address.offset
	length = address.size
	return source[offset - memory.GLOBAL_OFFSET:offset + length - memory.GLOBAL_OFFSET]


def set_value(target: bytearray, source: Iterable[int], address: "MemoryAddress") -> None:
	offset = address.offset
	length = address.size
	target[offset - memory.GLOBAL_OFFSET:offset + length - memory.GLOBAL_OFFSET] = source


def copy_values(source: bytearray, source_address: "MemoryAddress", target: bytearray,
                target_address: "MemoryAddress") -> None:
	assert source_address.size == target_address.size
	source_offset = source_address.offset
	target_offset = target_address.offset
	length = source_address.size
	target[target_offset - memory.GLOBAL_OFFSET:target_offset + length - memory.GLOBAL_OFFSET] = \
		source[source_offset - memory.GLOBAL_OFFSET:source_offset + length - memory.GLOBAL_OFFSET]


def get_stat(stat: bytearray) -> int:
	return stat[0] << 8 | stat[1]


def write_file(file: str, save: bytearray) -> None:
	with open(file, 'wb') as f:
		f.write(save)


def load_save(file: str) -> bytearray:
	with open(file, 'rb') as f:
		save = bytearray(f.read())
	return save


def get_total_clocks(source: bytearray) -> int:
	return struct.unpack_from("<Q", source[memory.TOTAL_CLOCKS_OFFSET:])[0] & 0x7f_ff_ff_ff


def get_program_counter(source: bytearray) -> int:
	return (source[memory.PC_OFFSET + 1] << 8) | source[memory.PC_OFFSET]


def randomize_rdiv(source: bytearray, rng):
	random_clock = [rng.randint(0, 255) for _ in range(2)]
	source[memory.DIVISOR_OFFSET:memory.DIVISOR_OFFSET + 2] = random_clock


def get_current_pokemon_index(battle_save):
	current_pokemon_index = get_value(battle_save, memory.wPartyMenuCursor)[0]
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
