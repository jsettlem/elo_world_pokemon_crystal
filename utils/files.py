import struct
from typing import Iterable

from battle_x_as_crystal import reverse_characters
from constants import memory
from constants.memory import MemoryAddress


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


def copy_values(source: bytearray, source_address: "MemoryAddress", target: bytearray,  target_address: "MemoryAddress") -> None:
	assert source_address.size == target_address.size
	source_offset = source_address.offset
	target_offset = target_address.offset
	length = source_address.size
	target[target_offset - memory.GLOBAL_OFFSET:target_offset + length - memory.GLOBAL_OFFSET] = \
		source[source_offset - memory.GLOBAL_OFFSET:source_offset + length - memory.GLOBAL_OFFSET]


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

