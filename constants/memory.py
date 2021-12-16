from dataclasses import dataclass

GLOBAL_OFFSET = 0xBAF0
TOTAL_CLOCKS_OFFSET = 0x21F
PC_OFFSET = 0xC7
DIVISOR_OFFSET = 0x20E

NAME_LENGTH = 11
PLAYER_NAME_LENGTH = 8
BATTLE_MON_SIZE = 0x20
PARTY_STRUCT_SIZE = 0x30

NAME_TERMINATOR = 0x50


@dataclass
class MemoryAddress:
	offset: int
	size: int


wOtherTrainerClass = MemoryAddress(0xd22f, 1)
wOtherTrainerID = MemoryAddress(0xd231, 1)

wStringBuffer1 = MemoryAddress(0xd073, PLAYER_NAME_LENGTH)

wPlayerName = MemoryAddress(0xd47d, PLAYER_NAME_LENGTH)
playerNameEnd = MemoryAddress(0xd48d + PLAYER_NAME_LENGTH - 1, 1)

wPlayerGender = MemoryAddress(0xd472, 1)
wTextboxFrame = MemoryAddress(0xcfce, 1)

wOTParty = MemoryAddress(0xd280, 0x1ac)
wOTPartyCount = MemoryAddress(0xd280, 1)

enemyParty = [
	MemoryAddress(0xd288 + i * PARTY_STRUCT_SIZE, PARTY_STRUCT_SIZE) for i in range(6)
]

wPlayerParty = MemoryAddress(0xdcd7, 0x1ac)
wPlayerPartyCount = MemoryAddress(0xdcd7, 1)

playerParty = [
	MemoryAddress(0xdcdf + i * PARTY_STRUCT_SIZE, PARTY_STRUCT_SIZE) for i in range(6)
]

playerPartyNicks = [
	MemoryAddress(0xde41 + i * NAME_LENGTH, NAME_LENGTH) for i in range(6)
]
playerPartyOTs = [
	MemoryAddress(0xddff + i * NAME_LENGTH, PLAYER_NAME_LENGTH) for i in range(6)
]

wBattleMonNickname = MemoryAddress(0xc621, NAME_LENGTH)
wEnemyMonNickname = MemoryAddress(0xc616, NAME_LENGTH)
wBattleMon = MemoryAddress(0xc62c, BATTLE_MON_SIZE)
wEnemyMon = MemoryAddress(0xd206, BATTLE_MON_SIZE)
wEnemyMoveStruct = MemoryAddress(0xc608, 7)
wPlayerMoveStruct = MemoryAddress(0xc60f, 7)
wPlayerSubStatus1 = MemoryAddress(0xc668, 1)
wEnemySubStatus1 = MemoryAddress(0xc66d, 1)
wPlayerSubStatus2 = MemoryAddress(0xc669, 1)
wEnemySubStatus2 = MemoryAddress(0xc66e, 1)
wPlayerSubStatus3 = MemoryAddress(0xc66a, 1)
wEnemySubStatus3 = MemoryAddress(0xc66f, 1)
wPlayerSubStatus4 = MemoryAddress(0xc66b, 1)
wEnemySubStatus4 = MemoryAddress(0xc670, 1)
wPlayerSubStatus5 = MemoryAddress(0xc66c, 1)
wEnemySubStatus5 = MemoryAddress(0xc671, 1)
wCurPlayerMove = MemoryAddress(0xc6e3, 1)
wCurEnemyMove = MemoryAddress(0xc6e4, 1)
wLastPlayerCounterMove = MemoryAddress(0xc6f8, 1)
wLastEnemyCounterMove = MemoryAddress(0xc6f9, 1)
wLastPlayerMove = MemoryAddress(0xc71b, 1)
wLastEnemyMove = MemoryAddress(0xc71c, 1)
wPlayerRolloutCount = MemoryAddress(0xc672, 1)
wEnemyRolloutCount = MemoryAddress(0xc67a, 1)
wPlayerConfuseCount = MemoryAddress(0xc673, 1)
wEnemyConfuseCount = MemoryAddress(0xc67b, 1)
wPlayerToxicCount = MemoryAddress(0xc674, 1)
wEnemyToxicCount = MemoryAddress(0xc67c, 1)
wPlayerDisableCount = MemoryAddress(0xc675, 1)
wEnemyDisableCount = MemoryAddress(0xc67d, 1)
wPlayerEncoreCount = MemoryAddress(0xc676, 1)
wEnemyEncoreCount = MemoryAddress(0xc67e, 1)
wPlayerPerishCount = MemoryAddress(0xc677, 1)
wEnemyPerishCount = MemoryAddress(0xc67f, 1)
wPlayerFuryCutterCount = MemoryAddress(0xc678, 1)
wEnemyFuryCutterCount = MemoryAddress(0xc680, 1)
wPlayerProtectCount = MemoryAddress(0xc679, 1)
wEnemyProtectCount = MemoryAddress(0xc681, 1)
wPlayerScreens = MemoryAddress(0xc6ff, 1)
wEnemyScreens = MemoryAddress(0xc700, 1)
wPlayerDamageTaken = MemoryAddress(0xc682, 2)
wEnemyDamageTaken = MemoryAddress(0xc684, 2)
wPlayerStats = MemoryAddress(0xc6b6, 10)
wEnemyStats = MemoryAddress(0xc6c1, 10)
wPlayerStatLevels = MemoryAddress(0xc6cc, 7)
wEnemyStatLevels = MemoryAddress(0xc6d4, 7)
wPlayerTurnsTaken = MemoryAddress(0xc6dd, 1)
wEnemyTurnsTaken = MemoryAddress(0xc6dc, 1)
wPlayerSubstituteHP = MemoryAddress(0xc6df, 1)
wEnemySubstituteHP = MemoryAddress(0xc6e0, 1)
wDisabledMove = MemoryAddress(0xc6f5, 1)
wEnemyDisabledMove = MemoryAddress(0xc6f6, 1)
wCurPartyMon = MemoryAddress(0xd109, 1)
wCurOTMon = MemoryAddress(0xc663, 1)

wEnemyItemState = MemoryAddress(0xc6e6, 1)
wCurEnemyMoveNum = MemoryAddress(0xc6e9, 1)
wEnemyMinimized = MemoryAddress(0xc6fa, 1)
wAlreadyFailed = MemoryAddress(0xc6fb, 1)
wCurMoveNum = MemoryAddress(0xd0d5, 1)
wPartyMenuCursor = MemoryAddress(0xd0d8, 1)
wEnemySwitchMonIndex = MemoryAddress(0xc718, 1)

breakpoints = {
	"SetUpBattlePartyMenu": 0x52f7,
	"AI_Switch": 0x446c,
	"LostBattle": 0x538e,
	"WinTrainerBattle": 0x4fa4
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
	(wCurPartyMon, wCurOTMon),  # TODO: check that wcurpartymon is correct
	(wPlayerParty, wOTParty)
)
