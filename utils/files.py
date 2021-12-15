import struct
from typing import Iterable

from battle_x_as_crystal import reverse_characters
from constants import memory


def name_to_bytes(name: str, length: int = memory.POKEMON_NAME_LENGTH) -> Iterable[int]:
	return (reverse_characters[name[i]] if i < len(name) else memory.NAME_TERMINATOR for i in range(length))


def get_value(source: bytearray, offset: int, length: int) -> bytearray:
	return source[offset - memory.GLOBAL_OFFSET:offset + length - memory.GLOBAL_OFFSET]


def set_value(target: bytearray, offset: int, source: Iterable[int], length: int) -> None:
	target[offset - memory.GLOBAL_OFFSET:offset + length - memory.GLOBAL_OFFSET] = source


def copy_values(source: bytearray, source_offset: int, target: bytearray, target_offset: int, length: int) -> None:
	target[target_offset - memory.GLOBAL_OFFSET:target_offset + length - memory.GLOBAL_OFFSET] = source[
	                                                                                             source_offset - memory.GLOBAL_OFFSET:source_offset + length - memory.GLOBAL_OFFSET]


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