from rich.pretty import pprint


def parse_bess_savestate(save: bytearray):
	'''
	Parses a BESS (Best Effort Save State) v. 1.0 save file.
	This is the save state format used by SameBoy and various other GameBoy emulators.

	Save format specification (in Markdown format):
	## Specification

	Every integer used in the BESS specification is stored in Little Endian encoding.

	### BESS footer

	BESS works by appending a detectable footer at the end of an existing save state format. The footer uses the following format:

	| Offset from end of file | Content                                               |
	|-------------------------|-------------------------------------------------------|
	| -8                      | Offset to the first BESS Block, from the file's start |
	| -4                      | The ASCII string 'BESS'                               |

	### BESS blocks

	BESS uses a block format where each block contains the following header:

	| Offset | Content                               |
	|--------|---------------------------------------|
	| 0      | A four-letter ASCII identifier        |
	| 4      | Length of the block, excluding header |

	Every block is followed by another block, until the END block is reached. If an implementation encounters an unsupported block, it should be completely ignored (Should not have any effect and should not trigger a failure).

	#### NAME block

	The NAME block uses the `'NAME'` identifier, and is an optional block that contains the name of the emulator that created this save state. While optional, it is highly recommended to be included in every implementation – it allows the user to know which emulator and version is compatible with the native save state format contained in this file. When used, this block should come first.

	The length of the NAME block is variable, and it only contains the name and version of the originating emulator in ASCII.


	#### INFO block

	The INFO block uses the `'INFO'` identifier, and is an optional block that contains information about the ROM this save state originates from. When used, this block should come before `CORE` but after `NAME`. This block is 0x12 bytes long, and it follows this structure:

	| Offset | Content                                          |
	|--------|--------------------------------------------------|
	| 0x00   | Bytes 0x134-0x143 from the ROM (Title)           |
	| 0x10   | Bytes 0x14E-0x14F from the ROM (Global checksum) |

	#### CORE block

	The CORE block uses the `'CORE'` identifier, and is a required block that contains both core state information, as well as basic information about the BESS version used. This block must be the first block, unless the `NAME` or `INFO` blocks exist then it must come directly after them. An implementation should not enforce block order on blocks unknown to it for future compatibility.

	The length of the CORE block is 0xD0 bytes, but implementations are expected to ignore any excess bytes. Following the BESS block header, the structure is as follows:

	| Offset | Content                                |
	|--------|----------------------------------------|
	| 0x00   | Major BESS version as a 16-bit integer |
	| 0x02   | Minor BESS version as a 16-bit integer |

	Both major and minor versions should be 1. Implementations are expected to reject incompatible majors, but still attempt to read newer minor versions.

	| Offset | Content                                |
	|--------|----------------------------------------|
	| 0x04   | A four-character ASCII model identifier |

	BESS uses a four-character string to identify Game Boy models:

	 * The first letter represents mutually-incompatible families of models and is required. The allowed values are `'G'` for the original Game Boy family, `'S'` for the Super Game Boy family, and `'C'` for the Game Boy Color and Advance family.
	* The second letter represents a specific model within the family, and is optional (If an implementation does not distinguish between specific models in a family, a space character may be used). The allowed values for family G are `'D'` for DMG and `'M'` for MGB; the allowed values for family S are `'N'` for NTSC, `'P'` for PAL, and `'2'` for SGB2; and the allowed values for family C are `'C'` for CGB, and `'A'` for the various GBA line models.
	* The third letter represents a specific CPU revision within a model, and is optional (If an implementation does not distinguish between revisions, a space character may be used). The allowed values for model GD (DMG) are `'0'` and `'A'`, through `'C'`; the allowed values for model CC (CGB) are `'0'` and `'A'`, through `'E'`; the allowed values for model CA (AGB, AGS, GBP) are `'0'`, `'A'` and `'B'`; and for every other model this value must be a space character.
	* The last character is used for padding and must be a space character.

	For example; `'GD  '` represents a DMG of an unspecified revision, `'S   '` represents some model of the SGB family, and `'CCE '` represent a CGB using CPU revision E.

	| Offset | Content                                                |
	|--------|--------------------------------------------------------|
	| 0x08   | The value of the PC register                           |
	| 0x0A   | The value of the AF register                           |
	| 0x0C   | The value of the BC register                           |
	| 0x0E   | The value of the DE register                           |
	| 0x10   | The value of the HL register                           |
	| 0x12   | The value of the SP register                           |
	| 0x14   | The value of IME (0 or 1)                              |
	| 0x15   | The value of the IE register                           |
	| 0x16   | Execution state (0 = running; 1 = halted; 2 = stopped) |
	| 0x17   | Reserved, must be 0                                    |
	| 0x18   | The values of every memory-mapped register (128 bytes) |

	The values of memory-mapped registers should be written 'as-is' to memory as if the actual ROM wrote them, with the following exceptions and note:
	* Unused registers have Don't-Care values which should be ignored
	* Unused register bits have Don't-Care values which should be ignored
	* If the model is CGB or newer, the value of KEY0 (FF4C) must be valid as it determines DMG mode
		* Bit 2 determines DMG mode. A value of 0x04 usually denotes DMG mode, while a value of `0x80` usually denotes CGB mode.
	* Object priority is derived from KEY0 (FF4C) instead of OPRI (FF6C) because OPRI can be modified after booting, but only the value of OPRI during boot ROM execution takes effect
	* If a register doesn't exist on the emulated model (For example, KEY0 (FF4C) on a DMG), its value should be ignored.
	* BANK (FF50) should be 0 if the boot ROM is still mapped, and 1 otherwise, and must be valid.
	* Implementations should not start a serial transfer when writing the value of SB
	* Similarly, no value of NRx4 should trigger a sound pulse on save state load
	* And similarly again, implementations should not trigger DMA transfers when writing the values of DMA or HDMA5
	* The value store for DIV will be used to set the internal divisor to `DIV << 8`
	* Implementation should apply care when ordering the write operations (For example, writes to NR52 must come before writes to the other APU registers)

	| Offset | Content                                                            |
	|--------|--------------------------------------------------------------------|
	| 0x98   | The size of RAM (32-bit integer)                                   |
	| 0x9C   | The offset of RAM from file start (32-bit integer)                 |
	| 0xA0   | The size of VRAM (32-bit integer)                                  |
	| 0xA4   | The offset of VRAM from file start (32-bit integer)                |
	| 0xA8   | The size of MBC RAM (32-bit integer)                               |
	| 0xAC   | The offset of MBC RAM from file start (32-bit integer)             |
	| 0xB0   | The size of OAM (=0xA0, 32-bit integer)                            |
	| 0xB4   | The offset of OAM from file start (32-bit integer)                 |
	| 0xB8   | The size of HRAM (=0x7F, 32-bit integer)                           |
	| 0xBC   | The offset of HRAM from file start (32-bit integer)                |
	| 0xC0   | The size of background palettes (=0x40 or 0, 32-bit integer)       |
	| 0xC4   | The offset of background palettes from file start (32-bit integer) |
	| 0xC8   | The size of object palettes (=0x40 or 0, 32-bit integer)           |
	| 0xCC   | The offset of object palettes from file start (32-bit integer)     |

	The contents of large buffers are stored outside of BESS structure so data from an implementation's native save state format can be reused. The offsets are absolute offsets from the save state file's start. Background and object palette sizes must be 0 for models prior to Game Boy Color.

	An implementation needs handle size mismatches gracefully. For example, if too large MBC RAM size is specified, the superfluous data should be ignored. On the other hand, if a too small VRAM size is specified (For example, if it's a save state from an emulator emulating a CGB in DMG mode, and it didn't save the second CGB VRAM bank), the implementation is expected to set that extra bank to all zeros.
	'''
	# Check for BESS footer
	if save[-4:] != b'BESS':
		raise ValueError('Not a BESS save state')

	# Get offset to first BESS block
	offset = int.from_bytes(save[-8:-4], 'little')

	# Parse BESS blocks
	blocks = {}
	while True:
		# Get block identifier
		identifier = save[offset:offset + 4].decode('ascii')
		if identifier == 'END ':
			break

		# Get block length
		length = int.from_bytes(save[offset + 4:offset + 8], 'little')

		# Get block data
		data = save[offset + 8:offset + 8 + length]

		# Add block to dictionary
		blocks[identifier] = data

		# Move to next block
		offset += 8 + length

	# Parse CORE block
	core = blocks['CORE']
	major_version = int.from_bytes(core[0:2], 'little')
	minor_version = int.from_bytes(core[2:4], 'little')
	model = core[4:8].decode('ascii')
	pc = int.from_bytes(core[8:10], 'little')
	af = int.from_bytes(core[10:12], 'little')
	bc = int.from_bytes(core[12:14], 'little')
	de = int.from_bytes(core[14:16], 'little')
	hl = int.from_bytes(core[16:18], 'little')
	sp = int.from_bytes(core[18:20], 'little')
	ime = bool(core[20])
	ie = int.from_bytes(core[21:22], 'little')
	state = int.from_bytes(core[22:23], 'little')
	registers = core[24:152]
	ram_size = int.from_bytes(core[152:156], 'little')
	ram_offset = int.from_bytes(core[156:160], 'little')
	vram_size = int.from_bytes(core[160:164], 'little')
	vram_offset = int.from_bytes(core[164:168], 'little')
	mbc_ram_size = int.from_bytes(core[168:172], 'little')
	mbc_ram_offset = int.from_bytes(core[172:176], 'little')
	oam_size = int.from_bytes(core[176:180], 'little')
	oam_offset = int.from_bytes(core[180:184], 'little')
	hram_size = int.from_bytes(core[184:188], 'little')
	hram_offset = int.from_bytes(core[188:192], 'little')
	bg_palette_size = int.from_bytes(core[192:196], 'little')
	bg_palette_offset = int.from_bytes(core[196:200], 'little')
	obj_palette_size = int.from_bytes(core[200:204], 'little')
	obj_palette_offset = int.from_bytes(core[204:208], 'little')

	# Parse INFO block
	if 'INFO' in blocks:
		info = blocks['INFO']
		title = info[0:16].decode('ascii', errors="ignore")
		checksum = int.from_bytes(info[16:18], 'little')
	else:
		title = None
		checksum = None

	# Parse NAME block
	if 'NAME' in blocks:
		name = blocks['NAME'].decode('ascii')
	else:
		name = None

	# Parse RAM
	ram = save[ram_offset:ram_offset + ram_size]

	# Parse VRAM
	vram = save[vram_offset:vram_offset + vram_size]

	# Parse MBC RAM
	mbc_ram = save[mbc_ram_offset:mbc_ram_offset + mbc_ram_size]

	# Parse OAM
	oam = save[oam_offset:oam_offset + oam_size]

	# Parse HRAM
	hram = save[hram_offset:hram_offset + hram_size]

	# Parse background palettes
	bg_palettes = save[bg_palette_offset:bg_palette_offset + bg_palette_size]

	# Parse object palettes
	obj_palettes = save[obj_palette_offset:obj_palette_offset + obj_palette_size]

	# Return parsed data
	return {
		'major_version': major_version,
		'minor_version': minor_version,
		'model': model,
		'pc': pc,
		'af': af,
		'bc': bc,
		'de': de,
		'hl': hl,
		'sp': sp,
		'ime': ime,
		'ie': ie,
		'state': state,
		'registers': registers,
		'ram_size': ram_size,
		'ram_offset': ram_offset,
		'vram_size': vram_size,
		'vram_offset': vram_offset,
		'mbc_ram_size': mbc_ram_size,
		'mbc_ram_offset': mbc_ram_offset,
		'oam_size': oam_size,
		'oam_offset': oam_offset,
		'hram_size': hram_size,
		'hram_offset': hram_offset,
		'bg_palette_size': bg_palette_size,
		'bg_palette_offset': bg_palette_offset,
		'obj_palette_size': obj_palette_size,
		'obj_palette_offset': obj_palette_offset,
		'title': title,
		'checksum': checksum,
		'name': name,
		'ram': ram,
		'vram': vram,
		'mbc_ram': mbc_ram
	}

if __name__ == '__main__':
	with open("./static_files/bgb_1_5_9/base_state_1.sna", "rb") as f:
		save = f.read()

	pprint(parse_bess_savestate(save))