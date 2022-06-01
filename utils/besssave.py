import struct
from random import Random
from typing import Iterable

from constants import memory
from constants.memory import MemoryAddress

class BessSave:
	def __init__(self, savestate: bytearray):
		self.save = savestate.copy()

		# Check for BESS footer
		if self.save[-4:] != b'BESS':
			raise ValueError('Not a BESS save state')

		# Get offset to first BESS block
		offset = int.from_bytes(self.save[-8:-4], 'little')

		# Parse BESS blocks
		self.blocks = {}
		while True:
			# Get block identifier
			identifier = self.save[offset:offset + 4].decode('ascii')
			if identifier == 'END ':
				break

			# Get block length
			length = int.from_bytes(self.save[offset + 4:offset + 8], 'little')

			# Get block data
			data = self.save[offset + 8:offset + 8 + length]

			# Add block to dictionary
			self.blocks[identifier] = data

			# Move to next block
			offset += 8 + length

		core = self.blocks['CORE']

		self.pc = int.from_bytes(core[8:10], 'little')

		self.ram_offset = int.from_bytes(core[156:160], 'little')

		self.total_clocks_offset = self.save.index(b'totalclks') + 0xE

		self.divisor_offset = self.save.index(b'divider') + 0xD

	def get_value(self, address: "MemoryAddress") -> bytearray:
		offset = address.offset
		length = address.size
		return self.save[offset + self.ram_offset - memory.WRAM_OFFSET:offset + length + self.ram_offset - memory.WRAM_OFFSET]

	def set_value(self, source: Iterable[int], address: "MemoryAddress") -> None:
		offset = address.offset
		length = address.size
		self.save[offset + self.ram_offset - memory.WRAM_OFFSET:offset + length + self.ram_offset - memory.WRAM_OFFSET] = bytearray(source)

	def copy_values(self, source_address: "MemoryAddress", target: "BessSave", target_address: "MemoryAddress") -> None:
		assert source_address.size == target_address.size
		target.set_value(self.get_value(source_address), target_address)

	def get_total_clocks(self) -> int:
		return struct.unpack_from("<Q", self.save[self.total_clocks_offset:])[0] & 0x7f_ff_ff_ff

	def get_program_counter(self) -> int:
		return self.pc

	def randomize_rdiv(self, rng: "Random") -> None:
		random_clock = [rng.randint(0, 255) for _ in range(2)]
		self.save[self.divisor_offset:self.divisor_offset + 2] = random_clock

	def copy(self) -> "BessSave":
		return BessSave(self.save)