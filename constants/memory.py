import os
import re
from dataclasses import dataclass
from typing import Dict, Tuple


def load_sym_file(filename):
	rom_symbols = {}
	reverse_rom_symbols = {}
	if os.path.isfile(filename):
		with open(filename) as f:
			for _line in f.readlines():
				line = _line.strip()
				if line == "":
					continue
				elif line.startswith(";"):
					continue
				elif line.startswith("["):
					# Start of key group
					# [labels]
					# [definitions]
					continue

				try:
					bank, addr, sym_label = re.split(":| ", line.strip())
					bank = int(bank, 16)
					addr = int(addr, 16)
					if not bank in rom_symbols:
						rom_symbols[bank] = {}

					rom_symbols[bank][addr] = sym_label
					reverse_rom_symbols[sym_label] = (bank, addr)
				except ValueError as ex:
					print(f"Skipping .sym line: {line.strip()}")
	return rom_symbols, reverse_rom_symbols

def reverse_symbol_map(symbols) -> Dict[str, Tuple[int, int]]:
	reverse_symbols = {}
	for bank in symbols:
		for addr in symbols[bank]:
			sym_label = symbols[bank][addr]
			reverse_symbols[sym_label] = (bank, addr)
	return reverse_symbols

symbols, reverse_symbols = load_sym_file("./static_files/pokecrystal11.sym")

WRAM_OFFSET = 0xC000

NAME_LENGTH = 11
PLAYER_NAME_LENGTH = 8
BATTLE_MON_SIZE = 0x20
PARTY_STRUCT_SIZE = 0x30

NAME_TERMINATOR = 0x50


@dataclass
class MemoryAddress:
	offset: int
	size: int

	def __init__(self, offset: str | int, size: int):
		if isinstance(offset, str):
			self.offset = reverse_symbols[offset][1]
		else:
			self.offset = offset
		self.size = size



wOtherTrainerClass = MemoryAddress("wOtherTrainerClass", 1)
wTrainerClass = MemoryAddress("wTrainerClass", 1)
wOtherTrainerID = MemoryAddress("wOtherTrainerID", 1)

wStringBuffer1 = MemoryAddress("wStringBuffer1", PLAYER_NAME_LENGTH)

wPlayerName = MemoryAddress("wPlayerName", PLAYER_NAME_LENGTH)
playerNameEnd = MemoryAddress(0xd48d + PLAYER_NAME_LENGTH - 1, 1)

wPlayerGender = MemoryAddress("wPlayerGender", 1)
wTextboxFrame = MemoryAddress("wTextboxFrame", 1)

wOTParty = MemoryAddress("wOTPartyCount", 0x1ac)
wOTPartyCount = MemoryAddress("wOTPartyCount", 1)

enemyParty = [
	MemoryAddress(reverse_symbols["wOTPartyMons"][1] + i * PARTY_STRUCT_SIZE, PARTY_STRUCT_SIZE) for i in range(6)
]

wPlayerParty = MemoryAddress("wPokemonData", 0x1ac)
wPlayerPartyCount = MemoryAddress("wPartyCount", 1)

playerParty = [
	MemoryAddress(reverse_symbols["wPartyMons"][1] + i * PARTY_STRUCT_SIZE, PARTY_STRUCT_SIZE) for i in range(6)
]

playerPartyNicks = [
	MemoryAddress(reverse_symbols["wPartyMonNicknames"][1] + i * NAME_LENGTH, NAME_LENGTH) for i in range(6)
]
playerPartyOTs = [
	MemoryAddress(reverse_symbols["wPartyMonOTs"][1] + i * NAME_LENGTH, PLAYER_NAME_LENGTH) for i in range(6)
]

wBattleMonNickname = MemoryAddress("wBattleMonNickname", NAME_LENGTH)
wEnemyMonNickname = MemoryAddress("wEnemyMonNickname", NAME_LENGTH)
wBattleMon = MemoryAddress("wBattleMon", BATTLE_MON_SIZE)
wEnemyMon = MemoryAddress("wEnemyMon", BATTLE_MON_SIZE)
wEnemyMoveStruct = MemoryAddress("wEnemyMoveStruct", 7)
wPlayerMoveStruct = MemoryAddress("wPlayerMoveStruct", 7)
wPlayerSubStatus1 = MemoryAddress("wPlayerSubStatus1", 1)
wEnemySubStatus1 = MemoryAddress("wEnemySubStatus1", 1)
wPlayerSubStatus2 = MemoryAddress("wPlayerSubStatus2", 1)
wEnemySubStatus2 = MemoryAddress("wEnemySubStatus2", 1)
wPlayerSubStatus3 = MemoryAddress("wPlayerSubStatus3", 1)
wEnemySubStatus3 = MemoryAddress("wEnemySubStatus3", 1)
wPlayerSubStatus4 = MemoryAddress("wPlayerSubStatus4", 1)
wEnemySubStatus4 = MemoryAddress("wEnemySubStatus4", 1)
wPlayerSubStatus5 = MemoryAddress("wPlayerSubStatus5", 1)
wEnemySubStatus5 = MemoryAddress("wEnemySubStatus5", 1)
wCurPlayerMove = MemoryAddress("wCurPlayerMove", 1)
wCurEnemyMove = MemoryAddress("wCurEnemyMove", 1)
wLastPlayerCounterMove = MemoryAddress("wLastPlayerCounterMove", 1)
wLastEnemyCounterMove = MemoryAddress("wLastEnemyCounterMove", 1)
wLastPlayerMove = MemoryAddress("wLastPlayerMove", 1)
wLastEnemyMove = MemoryAddress("wLastEnemyMove", 1)
wPlayerRolloutCount = MemoryAddress("wPlayerRolloutCount", 1)
wEnemyRolloutCount = MemoryAddress("wEnemyRolloutCount", 1)
wPlayerConfuseCount = MemoryAddress("wPlayerConfuseCount", 1)
wEnemyConfuseCount = MemoryAddress("wEnemyConfuseCount", 1)
wPlayerToxicCount = MemoryAddress("wPlayerToxicCount", 1)
wEnemyToxicCount = MemoryAddress("wEnemyToxicCount", 1)
wPlayerDisableCount = MemoryAddress("wPlayerDisableCount", 1)
wEnemyDisableCount = MemoryAddress("wEnemyDisableCount", 1)
wPlayerEncoreCount = MemoryAddress("wPlayerEncoreCount", 1)
wEnemyEncoreCount = MemoryAddress("wEnemyEncoreCount", 1)
wPlayerPerishCount = MemoryAddress("wPlayerPerishCount", 1)
wEnemyPerishCount = MemoryAddress("wEnemyPerishCount", 1)
wPlayerFuryCutterCount = MemoryAddress("wPlayerFuryCutterCount", 1)
wEnemyFuryCutterCount = MemoryAddress("wEnemyFuryCutterCount", 1)
wPlayerProtectCount = MemoryAddress("wPlayerProtectCount", 1)
wEnemyProtectCount = MemoryAddress("wEnemyProtectCount", 1)
wPlayerScreens = MemoryAddress("wPlayerScreens", 1)
wEnemyScreens = MemoryAddress("wEnemyScreens", 1)
wPlayerDamageTaken = MemoryAddress("wPlayerDamageTaken", 2)
wEnemyDamageTaken = MemoryAddress("wEnemyDamageTaken", 2)
wPlayerStats = MemoryAddress("wPlayerStats", 10)
wEnemyStats = MemoryAddress("wEnemyStats", 10)
wPlayerStatLevels = MemoryAddress("wPlayerStatLevels", 7)
wEnemyStatLevels = MemoryAddress("wEnemyStatLevels", 7)
wPlayerTurnsTaken = MemoryAddress("wPlayerTurnsTaken", 1)
wEnemyTurnsTaken = MemoryAddress("wEnemyTurnsTaken", 1)
wPlayerSubstituteHP = MemoryAddress("wPlayerSubstituteHP", 1)
wEnemySubstituteHP = MemoryAddress("wEnemySubstituteHP", 1)
wDisabledMove = MemoryAddress("wDisabledMove", 1)
wEnemyDisabledMove = MemoryAddress("wEnemyDisabledMove", 1)
wCurPartyMon = MemoryAddress("wCurPartyMon", 1)
wCurBattleMon = MemoryAddress("wCurBattleMon", 1)
wCurOTMon = MemoryAddress("wCurOTMon", 1)

wPlayerTrappingMove = MemoryAddress("wPlayerTrappingMove", 1)
wEnemyTrappingMove = MemoryAddress("wEnemyTrappingMove" , 1)
wPlayerWrapCount = MemoryAddress("wPlayerWrapCount", 1)
wEnemyWrapCount = MemoryAddress("wEnemyWrapCount", 1)
wPlayerCharging = MemoryAddress("wPlayerCharging", 1)
wEnemyCharging = MemoryAddress("wEnemyCharging", 1)
wPlayerRageCounter = MemoryAddress("wPlayerRageCounter", 1)
wEnemyRageCounter = MemoryAddress("wEnemyRageCounter", 1)
wPlayerMinimized = MemoryAddress("wPlayerMinimized", 1)
wEnemyMinimized = MemoryAddress("wEnemyMinimized", 1)

wEnemyItemState = MemoryAddress("wEnemyItemState", 1)
wCurEnemyMoveNum = MemoryAddress("wCurEnemyMoveNum", 1)
wAlreadyFailed = MemoryAddress("wAlreadyFailed", 1)
wCurMoveNum = MemoryAddress("wCurMoveNum", 1)
wPartyMenuCursor = MemoryAddress("wPartyMenuCursor", 1)
wEnemySwitchMonIndex = MemoryAddress("wEnemySwitchMonIndex", 1)

wBattleWeather = MemoryAddress("wBattleWeather", 1)

breakpoints = {
	"SetUpBattlePartyMenu": 0x52f7,
	"AI_Switch": 0x446c,
	"LostBattle": 0x538e,
	"WinTrainerBattle": 0x4fa4
}

usedFullHeal = 0x43a3
usedMaxPotion = 0x43ae
usedFullRestore = 0x43b5
usedPotion = 0x43e8
usedSuperPotion = 0x43ee
usedHyperPotion = 0x43f4
usedXAccuracy = 0x44f7
usedGuardSpec = 0x4504
usedDireHit = 0x4511
usedXAttack = 0x4541
usedXDefend = 0x4547
usedXSpeed = 0x454d
usedXSpecial = 0x4553

itemFullHeal = 0x26
itemMaxPotion = 0x0f
itemFullRestore = 0x0e
itemPotion = 0x12
itemSuperPotion = 0x11
itemHyperPotion = 0x10
itemXAccuracy = 0x21
itemGuardSpec = 0x29
itemDireHit = 0x2c
itemXAttack = 0x31
itemXDefend = 0x33
itemXSpeed = 0x34
itemXSpecial = 0x35

items = {
	usedFullHeal: itemFullHeal,
	usedMaxPotion: itemMaxPotion,
	usedFullRestore: itemFullRestore,
	usedPotion: itemPotion,
	usedSuperPotion: itemSuperPotion,
	usedHyperPotion: itemHyperPotion,
	usedXAccuracy: itemXAccuracy,
	usedGuardSpec: itemGuardSpec,
	usedDireHit: itemDireHit,
	usedXAttack: itemXAttack,
	usedXDefend: itemXDefend,
	usedXSpeed: itemXSpeed,
	usedXSpecial: itemXSpecial
}

player_enemy_pairs = (
	(wBattleMonNickname, wEnemyMonNickname),
	(wBattleMon, wEnemyMon),
	(wPlayerMoveStruct, wEnemyMoveStruct),
	(wPlayerSubStatus1, wEnemySubStatus1),
	(wPlayerSubStatus2, wEnemySubStatus2),
	(wPlayerSubStatus3, wEnemySubStatus3),
	(wPlayerSubStatus4, wEnemySubStatus4),
	(wPlayerSubStatus5, wEnemySubStatus5),
	(wCurPlayerMove, wCurEnemyMove),
	(wLastPlayerCounterMove, wLastEnemyCounterMove),
	(wLastPlayerMove, wLastEnemyMove),
	(wPlayerRolloutCount, wEnemyRolloutCount),
	(wPlayerConfuseCount, wEnemyConfuseCount),
	(wPlayerToxicCount, wEnemyToxicCount),
	(wPlayerDisableCount, wEnemyDisableCount),
	(wPlayerEncoreCount, wEnemyEncoreCount),
	(wPlayerPerishCount, wEnemyPerishCount),
	(wPlayerFuryCutterCount, wEnemyFuryCutterCount),
	(wPlayerProtectCount, wEnemyProtectCount),
	(wPlayerScreens, wEnemyScreens),
	(wPlayerDamageTaken, wEnemyDamageTaken),
	(wPlayerStats, wEnemyStats),
	(wPlayerStatLevels, wEnemyStatLevels),
	(wPlayerTurnsTaken, wEnemyTurnsTaken),
	(wPlayerSubstituteHP, wEnemySubstituteHP),
	(wDisabledMove, wEnemyDisabledMove),
	(wCurPartyMon, wCurOTMon),
	(wCurBattleMon, wCurOTMon),# TODO: check that wcurbattlemon is correct
	(wPlayerParty, wOTParty),
	(wPlayerTrappingMove, wEnemyTrappingMove),
	(wPlayerWrapCount, wEnemyWrapCount),
	(wPlayerCharging, wEnemyCharging),
	(wPlayerRageCounter, wEnemyRageCounter),
	(wPlayerMinimized, wEnemyMinimized),
)


wPlayerUsedMoves = MemoryAddress("wPlayerUsedMoves", 4)
wEnemyMonMoves = MemoryAddress("wEnemyMonMoves", 4)
wEnemyMonPP = MemoryAddress("wEnemyMonPP", 4)

wBattleMonMoves = MemoryAddress("wBattleMonMoves", 4)

wNumItems = MemoryAddress("wNumItems", 1)
wItems = MemoryAddress("wItems", 3)
wEnemyTrainerItems = MemoryAddress("wEnemyTrainerItem1", 2)

wBattleMonSpecies = MemoryAddress("wBattleMonSpecies", 1)
wBattleMonHP = MemoryAddress("wBattleMonHP", 2)
wBattleMonMaxHP = MemoryAddress("wBattleMonMaxHP", 2)

wEnemyMonSpecies = MemoryAddress("wEnemyMonSpecies", 1)
wEnemyMonHP = MemoryAddress("wEnemyMonHP", 2)
wEnemyMonMaxHP = MemoryAddress("wEnemyMonMaxHP", 2)

wEnemyTrainerBaseReward = MemoryAddress("wEnemyTrainerBaseReward", 1)
