GLOBAL_OFFSET = 0xBAF0
TOTAL_CLOCKS_OFFSET = 0x21F
PC_OFFSET = 0xC7

OTHER_TRAINER_CLASS = 0xd22f
# TRAINER_CLASS = 0xd233
TRAINER_ID = 0xd231

STRING_BUFFER_1 = 0xd073

ENEMY_NAME_LENGTH = 11
POKEMON_NAME_LENGTH = 11
NAME_TERMINATOR = 0x50

PLAYER_TRAINER_NAME = 0xd47d
PLAYER_NAME_LENGTH = 8

PLAYER_GENDER = 0xd472

PARTY_STRUCT_SIZE = 0x30
BATTLE_MON_SIZE = 0x20

ENEMY_PARTY_START = 0xd280
ENEMY_PARTY_STRUCTS_START = 0xd288
ENEMY_PARTY_COUNT = 0xd280
ENEMY_PARTY_NICKS = 0xd3ea
MON_NICK_LENGTH = 11
ENEMY_PARTY_END = 0xd42c

PLAYER_PARTY_START = 0xdcd7
PLAYER_PARTY_COUNT = 0xdcd7
PLAYER_PARTY_STURCTS_START = 0xdcdf
PLAYER_PARTY_NICKS = 0xde41
PLAYER_PARTY_OTS = 0xddff
PLAYER_PARTY_END = 0xde83

wBattleMonNickname = (0xc621, POKEMON_NAME_LENGTH)
wEnemyMonNickname = (0xc616, POKEMON_NAME_LENGTH)

wBattleMon = (0xc62c, BATTLE_MON_SIZE)
wEnemyMon = (0xd206, BATTLE_MON_SIZE)
wEnemyMoveStruct = (0xc608, 7)
wPlayerMoveStruct = (0xc60f, 7)

wPlayerSubStatus1 = (0xc668, 1)
wEnemySubStatus1 = (0xc66d, 1)
wPlayerSubStatus2 = (0xc669, 1)
wEnemySubStatus2 = (0xc66e, 1)
wPlayerSubStatus3 = (0xc66a, 1)
wEnemySubStatus3 = (0xc66f, 1)
wPlayerSubStatus4 = (0xc66b, 1)
wEnemySubStatus4 = (0xc670, 1)
wPlayerSubStatus5 = (0xc66c, 1)
wEnemySubStatus5 = (0xc671, 1)

wCurPlayerMove = (0xc6e3, 1)
wCurEnemyMove = (0xc6e4, 1)
wLastPlayerCounterMove = (0xc6f8, 1)
wLastEnemyCounterMove = (0xc6f9, 1)
wLastPlayerMove = (0xc71b, 1)
wLastEnemyMove = (0xc71c, 1)
wPlayerRolloutCount = (0xc672, 1)
wEnemyRolloutCount = (0xc67a, 1)
wPlayerConfuseCount = (0xc673, 1)
wEnemyConfuseCount = (0xc67b, 1)
wPlayerToxicCount = (0xc674, 1)
wEnemyToxicCount = (0xc67c, 1)
wPlayerDisableCount = (0xc675, 1)
wEnemyDisableCount = (0xc67d, 1)
wPlayerEncoreCount = (0xc676, 1)
wEnemyEncoreCount = (0xc67e, 1)
wPlayerPerishCount = (0xc677, 1)
wEnemyPerishCount = (0xc67f, 1)
wPlayerFuryCutterCount = (0xc678, 1)
wEnemyFuryCutterCount = (0xc680, 1)
wPlayerProtectCount = (0xc679, 1)
wEnemyProtectCount = (0xc681, 1)
wPlayerScreens = (0xc6ff, 1)
wEnemyScreens = (0xc700, 1)
wPlayerDamageTaken = (0xc682, 2)
wEnemyDamageTaken = (0xc684, 2)
wPlayerStats = (0xc6b6, 10)
wEnemyStats = (0xc6c1, 10)
wPlayerStatLevels = (0xc6cc, 7)
wEnemyStatLevels = (0xc6d4, 7)
wPlayerTurnsTaken = (0xc6dd, 1)
wEnemyTurnsTaken = (0xc6dc, 1)
wPlayerSubstituteHP = (0xc6df, 1)
wEnemySubstituteHP = (0xc6e0, 1)
wDisabledMove = (0xc6f5, 1)
wEnemyDisabledMove = (0xc6f6, 1)

wCurPartyMon = (0xd109, 1)
wCurOTMon = (0xc663, 1)

wEnemyItemState = (0xc6e6, 1)
wCurEnemyMoveNum = (0xc6e9, 1)
wEnemyMinimized = (0xc6fa, 1)
wAlreadyFailed = (0xc6fb, 1)
wCurMoveNum = (0xd0d5, 1)

wPartyMenuCursor = (0xd0d8, 1)
wEnemySwitchMonIndex = (0xc718, 1)

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
	(wCurPartyMon, wCurOTMon)  # TODO: check that wcurpartymon is correct
)
