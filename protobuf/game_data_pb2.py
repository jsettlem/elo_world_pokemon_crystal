# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game_data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fgame_data.proto*\xf4\x1d\n\x0eMoveIdentifier\x12\x10\n\x0cUNKNOWN_MOVE\x10\x00\x12\t\n\x05POUND\x10\x01\x12\x0f\n\x0bKARATE_CHOP\x10\x02\x12\x0e\n\nDOUBLESLAP\x10\x03\x12\x0f\n\x0b\x43OMET_PUNCH\x10\x04\x12\x0e\n\nMEGA_PUNCH\x10\x05\x12\x0b\n\x07PAY_DAY\x10\x06\x12\x0e\n\nFIRE_PUNCH\x10\x07\x12\r\n\tICE_PUNCH\x10\x08\x12\x10\n\x0cTHUNDERPUNCH\x10\t\x12\x0b\n\x07SCRATCH\x10\n\x12\x0c\n\x08VICEGRIP\x10\x0b\x12\x0e\n\nGUILLOTINE\x10\x0c\x12\x0e\n\nRAZOR_WIND\x10\r\x12\x10\n\x0cSWORDS_DANCE\x10\x0e\x12\x07\n\x03\x43UT\x10\x0f\x12\x08\n\x04GUST\x10\x10\x12\x0f\n\x0bWING_ATTACK\x10\x11\x12\r\n\tWHIRLWIND\x10\x12\x12\x07\n\x03\x46LY\x10\x13\x12\x08\n\x04\x42IND\x10\x14\x12\x08\n\x04SLAM\x10\x15\x12\r\n\tVINE_WHIP\x10\x16\x12\t\n\x05STOMP\x10\x17\x12\x0f\n\x0b\x44OUBLE_KICK\x10\x18\x12\r\n\tMEGA_KICK\x10\x19\x12\r\n\tJUMP_KICK\x10\x1a\x12\x10\n\x0cROLLING_KICK\x10\x1b\x12\x0f\n\x0bSAND_ATTACK\x10\x1c\x12\x0c\n\x08HEADBUTT\x10\x1d\x12\x0f\n\x0bHORN_ATTACK\x10\x1e\x12\x0f\n\x0b\x46URY_ATTACK\x10\x1f\x12\x0e\n\nHORN_DRILL\x10 \x12\n\n\x06TACKLE\x10!\x12\r\n\tBODY_SLAM\x10\"\x12\x08\n\x04WRAP\x10#\x12\r\n\tTAKE_DOWN\x10$\x12\n\n\x06THRASH\x10%\x12\x0f\n\x0b\x44OUBLE_EDGE\x10&\x12\r\n\tTAIL_WHIP\x10\'\x12\x10\n\x0cPOISON_STING\x10(\x12\r\n\tTWINEEDLE\x10)\x12\x0f\n\x0bPIN_MISSILE\x10*\x12\x08\n\x04LEER\x10+\x12\x08\n\x04\x42ITE\x10,\x12\t\n\x05GROWL\x10-\x12\x08\n\x04ROAR\x10.\x12\x08\n\x04SING\x10/\x12\x0e\n\nSUPERSONIC\x10\x30\x12\r\n\tSONICBOOM\x10\x31\x12\x0b\n\x07\x44ISABLE\x10\x32\x12\x08\n\x04\x41\x43ID\x10\x33\x12\t\n\x05\x45MBER\x10\x34\x12\x10\n\x0c\x46LAMETHROWER\x10\x35\x12\x08\n\x04MIST\x10\x36\x12\r\n\tWATER_GUN\x10\x37\x12\x0e\n\nHYDRO_PUMP\x10\x38\x12\x08\n\x04SURF\x10\x39\x12\x0c\n\x08ICE_BEAM\x10:\x12\x0c\n\x08\x42LIZZARD\x10;\x12\x0b\n\x07PSYBEAM\x10<\x12\x0e\n\nBUBBLEBEAM\x10=\x12\x0f\n\x0b\x41URORA_BEAM\x10>\x12\x0e\n\nHYPER_BEAM\x10?\x12\x08\n\x04PECK\x10@\x12\x0e\n\nDRILL_PECK\x10\x41\x12\x0e\n\nSUBMISSION\x10\x42\x12\x0c\n\x08LOW_KICK\x10\x43\x12\x0b\n\x07\x43OUNTER\x10\x44\x12\x10\n\x0cSEISMIC_TOSS\x10\x45\x12\x0c\n\x08STRENGTH\x10\x46\x12\n\n\x06\x41\x42SORB\x10G\x12\x0e\n\nMEGA_DRAIN\x10H\x12\x0e\n\nLEECH_SEED\x10I\x12\n\n\x06GROWTH\x10J\x12\x0e\n\nRAZOR_LEAF\x10K\x12\r\n\tSOLARBEAM\x10L\x12\x10\n\x0cPOISONPOWDER\x10M\x12\x0e\n\nSTUN_SPORE\x10N\x12\x10\n\x0cSLEEP_POWDER\x10O\x12\x0f\n\x0bPETAL_DANCE\x10P\x12\x0f\n\x0bSTRING_SHOT\x10Q\x12\x0f\n\x0b\x44RAGON_RAGE\x10R\x12\r\n\tFIRE_SPIN\x10S\x12\x10\n\x0cTHUNDERSHOCK\x10T\x12\x0f\n\x0bTHUNDERBOLT\x10U\x12\x10\n\x0cTHUNDER_WAVE\x10V\x12\x0b\n\x07THUNDER\x10W\x12\x0e\n\nROCK_THROW\x10X\x12\x0e\n\nEARTHQUAKE\x10Y\x12\x0b\n\x07\x46ISSURE\x10Z\x12\x07\n\x03\x44IG\x10[\x12\t\n\x05TOXIC\x10\\\x12\r\n\tCONFUSION\x10]\x12\r\n\tPSYCHIC_M\x10^\x12\x0c\n\x08HYPNOSIS\x10_\x12\x0c\n\x08MEDITATE\x10`\x12\x0b\n\x07\x41GILITY\x10\x61\x12\x10\n\x0cQUICK_ATTACK\x10\x62\x12\x08\n\x04RAGE\x10\x63\x12\x0c\n\x08TELEPORT\x10\x64\x12\x0f\n\x0bNIGHT_SHADE\x10\x65\x12\t\n\x05MIMIC\x10\x66\x12\x0b\n\x07SCREECH\x10g\x12\x0f\n\x0b\x44OUBLE_TEAM\x10h\x12\x0b\n\x07RECOVER\x10i\x12\n\n\x06HARDEN\x10j\x12\x0c\n\x08MINIMIZE\x10k\x12\x0f\n\x0bSMOKESCREEN\x10l\x12\x0f\n\x0b\x43ONFUSE_RAY\x10m\x12\x0c\n\x08WITHDRAW\x10n\x12\x10\n\x0c\x44\x45\x46\x45NSE_CURL\x10o\x12\x0b\n\x07\x42\x41RRIER\x10p\x12\x10\n\x0cLIGHT_SCREEN\x10q\x12\x08\n\x04HAZE\x10r\x12\x0b\n\x07REFLECT\x10s\x12\x10\n\x0c\x46OCUS_ENERGY\x10t\x12\x08\n\x04\x42IDE\x10u\x12\r\n\tMETRONOME\x10v\x12\x0f\n\x0bMIRROR_MOVE\x10w\x12\x10\n\x0cSELFDESTRUCT\x10x\x12\x0c\n\x08\x45GG_BOMB\x10y\x12\x08\n\x04LICK\x10z\x12\x08\n\x04SMOG\x10{\x12\n\n\x06SLUDGE\x10|\x12\r\n\tBONE_CLUB\x10}\x12\x0e\n\nFIRE_BLAST\x10~\x12\r\n\tWATERFALL\x10\x7f\x12\n\n\x05\x43LAMP\x10\x80\x01\x12\n\n\x05SWIFT\x10\x81\x01\x12\x0f\n\nSKULL_BASH\x10\x82\x01\x12\x11\n\x0cSPIKE_CANNON\x10\x83\x01\x12\x0e\n\tCONSTRICT\x10\x84\x01\x12\x0c\n\x07\x41MNESIA\x10\x85\x01\x12\x0c\n\x07KINESIS\x10\x86\x01\x12\x0f\n\nSOFTBOILED\x10\x87\x01\x12\x11\n\x0cHI_JUMP_KICK\x10\x88\x01\x12\n\n\x05GLARE\x10\x89\x01\x12\x10\n\x0b\x44REAM_EATER\x10\x8a\x01\x12\x0f\n\nPOISON_GAS\x10\x8b\x01\x12\x0c\n\x07\x42\x41RRAGE\x10\x8c\x01\x12\x0f\n\nLEECH_LIFE\x10\x8d\x01\x12\x10\n\x0bLOVELY_KISS\x10\x8e\x01\x12\x0f\n\nSKY_ATTACK\x10\x8f\x01\x12\x0e\n\tTRANSFORM\x10\x90\x01\x12\x0b\n\x06\x42UBBLE\x10\x91\x01\x12\x10\n\x0b\x44IZZY_PUNCH\x10\x92\x01\x12\n\n\x05SPORE\x10\x93\x01\x12\n\n\x05\x46LASH\x10\x94\x01\x12\x0c\n\x07PSYWAVE\x10\x95\x01\x12\x0b\n\x06SPLASH\x10\x96\x01\x12\x0f\n\nACID_ARMOR\x10\x97\x01\x12\x0f\n\nCRABHAMMER\x10\x98\x01\x12\x0e\n\tEXPLOSION\x10\x99\x01\x12\x10\n\x0b\x46URY_SWIPES\x10\x9a\x01\x12\x0f\n\nBONEMERANG\x10\x9b\x01\x12\t\n\x04REST\x10\x9c\x01\x12\x0f\n\nROCK_SLIDE\x10\x9d\x01\x12\x0f\n\nHYPER_FANG\x10\x9e\x01\x12\x0c\n\x07SHARPEN\x10\x9f\x01\x12\x0f\n\nCONVERSION\x10\xa0\x01\x12\x0f\n\nTRI_ATTACK\x10\xa1\x01\x12\x0f\n\nSUPER_FANG\x10\xa2\x01\x12\n\n\x05SLASH\x10\xa3\x01\x12\x0f\n\nSUBSTITUTE\x10\xa4\x01\x12\r\n\x08STRUGGLE\x10\xa5\x01\x12\x0b\n\x06SKETCH\x10\xa6\x01\x12\x10\n\x0bTRIPLE_KICK\x10\xa7\x01\x12\n\n\x05THIEF\x10\xa8\x01\x12\x0f\n\nSPIDER_WEB\x10\xa9\x01\x12\x10\n\x0bMIND_READER\x10\xaa\x01\x12\x0e\n\tNIGHTMARE\x10\xab\x01\x12\x10\n\x0b\x46LAME_WHEEL\x10\xac\x01\x12\n\n\x05SNORE\x10\xad\x01\x12\n\n\x05\x43URSE\x10\xae\x01\x12\n\n\x05\x46LAIL\x10\xaf\x01\x12\x10\n\x0b\x43ONVERSION2\x10\xb0\x01\x12\x0e\n\tAEROBLAST\x10\xb1\x01\x12\x11\n\x0c\x43OTTON_SPORE\x10\xb2\x01\x12\r\n\x08REVERSAL\x10\xb3\x01\x12\n\n\x05SPITE\x10\xb4\x01\x12\x10\n\x0bPOWDER_SNOW\x10\xb5\x01\x12\x0c\n\x07PROTECT\x10\xb6\x01\x12\x0f\n\nMACH_PUNCH\x10\xb7\x01\x12\x0f\n\nSCARY_FACE\x10\xb8\x01\x12\x11\n\x0c\x46\x41INT_ATTACK\x10\xb9\x01\x12\x0f\n\nSWEET_KISS\x10\xba\x01\x12\x0f\n\nBELLY_DRUM\x10\xbb\x01\x12\x10\n\x0bSLUDGE_BOMB\x10\xbc\x01\x12\r\n\x08MUD_SLAP\x10\xbd\x01\x12\x0e\n\tOCTAZOOKA\x10\xbe\x01\x12\x0b\n\x06SPIKES\x10\xbf\x01\x12\x0f\n\nZAP_CANNON\x10\xc0\x01\x12\x0e\n\tFORESIGHT\x10\xc1\x01\x12\x11\n\x0c\x44\x45STINY_BOND\x10\xc2\x01\x12\x10\n\x0bPERISH_SONG\x10\xc3\x01\x12\r\n\x08ICY_WIND\x10\xc4\x01\x12\x0b\n\x06\x44\x45TECT\x10\xc5\x01\x12\x0e\n\tBONE_RUSH\x10\xc6\x01\x12\x0c\n\x07LOCK_ON\x10\xc7\x01\x12\x0c\n\x07OUTRAGE\x10\xc8\x01\x12\x0e\n\tSANDSTORM\x10\xc9\x01\x12\x0f\n\nGIGA_DRAIN\x10\xca\x01\x12\x0b\n\x06\x45NDURE\x10\xcb\x01\x12\n\n\x05\x43HARM\x10\xcc\x01\x12\x0c\n\x07ROLLOUT\x10\xcd\x01\x12\x10\n\x0b\x46\x41LSE_SWIPE\x10\xce\x01\x12\x0c\n\x07SWAGGER\x10\xcf\x01\x12\x0f\n\nMILK_DRINK\x10\xd0\x01\x12\n\n\x05SPARK\x10\xd1\x01\x12\x10\n\x0b\x46URY_CUTTER\x10\xd2\x01\x12\x0f\n\nSTEEL_WING\x10\xd3\x01\x12\x0e\n\tMEAN_LOOK\x10\xd4\x01\x12\x0c\n\x07\x41TTRACT\x10\xd5\x01\x12\x0f\n\nSLEEP_TALK\x10\xd6\x01\x12\x0e\n\tHEAL_BELL\x10\xd7\x01\x12\x0b\n\x06RETURN\x10\xd8\x01\x12\x0c\n\x07PRESENT\x10\xd9\x01\x12\x10\n\x0b\x46RUSTRATION\x10\xda\x01\x12\x0e\n\tSAFEGUARD\x10\xdb\x01\x12\x0f\n\nPAIN_SPLIT\x10\xdc\x01\x12\x10\n\x0bSACRED_FIRE\x10\xdd\x01\x12\x0e\n\tMAGNITUDE\x10\xde\x01\x12\x11\n\x0c\x44YNAMICPUNCH\x10\xdf\x01\x12\r\n\x08MEGAHORN\x10\xe0\x01\x12\x11\n\x0c\x44RAGONBREATH\x10\xe1\x01\x12\x0f\n\nBATON_PASS\x10\xe2\x01\x12\x0b\n\x06\x45NCORE\x10\xe3\x01\x12\x0c\n\x07PURSUIT\x10\xe4\x01\x12\x0f\n\nRAPID_SPIN\x10\xe5\x01\x12\x10\n\x0bSWEET_SCENT\x10\xe6\x01\x12\x0e\n\tIRON_TAIL\x10\xe7\x01\x12\x0f\n\nMETAL_CLAW\x10\xe8\x01\x12\x10\n\x0bVITAL_THROW\x10\xe9\x01\x12\x10\n\x0bMORNING_SUN\x10\xea\x01\x12\x0e\n\tSYNTHESIS\x10\xeb\x01\x12\x0e\n\tMOONLIGHT\x10\xec\x01\x12\x11\n\x0cHIDDEN_POWER\x10\xed\x01\x12\x0f\n\nCROSS_CHOP\x10\xee\x01\x12\x0c\n\x07TWISTER\x10\xef\x01\x12\x0f\n\nRAIN_DANCE\x10\xf0\x01\x12\x0e\n\tSUNNY_DAY\x10\xf1\x01\x12\x0b\n\x06\x43RUNCH\x10\xf2\x01\x12\x10\n\x0bMIRROR_COAT\x10\xf3\x01\x12\r\n\x08PSYCH_UP\x10\xf4\x01\x12\x11\n\x0c\x45XTREMESPEED\x10\xf5\x01\x12\x11\n\x0c\x41NCIENTPOWER\x10\xf6\x01\x12\x10\n\x0bSHADOW_BALL\x10\xf7\x01\x12\x11\n\x0c\x46UTURE_SIGHT\x10\xf8\x01\x12\x0f\n\nROCK_SMASH\x10\xf9\x01\x12\x0e\n\tWHIRLPOOL\x10\xfa\x01\x12\x0c\n\x07\x42\x45\x41T_UP\x10\xfb\x01*\x95\x1b\n\x0ePokemonSpecies\x12\r\n\tBULBASAUR\x10\x00\x12\x0b\n\x07IVYSAUR\x10\x01\x12\x0c\n\x08VENUSAUR\x10\x02\x12\x0e\n\nCHARMANDER\x10\x03\x12\x0e\n\nCHARMELEON\x10\x04\x12\r\n\tCHARIZARD\x10\x05\x12\x0c\n\x08SQUIRTLE\x10\x06\x12\r\n\tWARTORTLE\x10\x07\x12\r\n\tBLASTOISE\x10\x08\x12\x0c\n\x08\x43\x41TERPIE\x10\t\x12\x0b\n\x07METAPOD\x10\n\x12\x0e\n\nBUTTERFREE\x10\x0b\x12\n\n\x06WEEDLE\x10\x0c\x12\n\n\x06KAKUNA\x10\r\x12\x0c\n\x08\x42\x45\x45\x44RILL\x10\x0e\x12\n\n\x06PIDGEY\x10\x0f\x12\r\n\tPIDGEOTTO\x10\x10\x12\x0b\n\x07PIDGEOT\x10\x11\x12\x0b\n\x07RATTATA\x10\x12\x12\x0c\n\x08RATICATE\x10\x13\x12\x0b\n\x07SPEAROW\x10\x14\x12\n\n\x06\x46\x45\x41ROW\x10\x15\x12\t\n\x05\x45KANS\x10\x16\x12\t\n\x05\x41RBOK\x10\x17\x12\x0b\n\x07PIKACHU\x10\x18\x12\n\n\x06RAICHU\x10\x19\x12\r\n\tSANDSHREW\x10\x1a\x12\r\n\tSANDSLASH\x10\x1b\x12\r\n\tNIDORAN_F\x10\x1c\x12\x0c\n\x08NIDORINA\x10\x1d\x12\r\n\tNIDOQUEEN\x10\x1e\x12\r\n\tNIDORAN_M\x10\x1f\x12\x0c\n\x08NIDORINO\x10 \x12\x0c\n\x08NIDOKING\x10!\x12\x0c\n\x08\x43LEFAIRY\x10\"\x12\x0c\n\x08\x43LEFABLE\x10#\x12\n\n\x06VULPIX\x10$\x12\r\n\tNINETALES\x10%\x12\x0e\n\nJIGGLYPUFF\x10&\x12\x0e\n\nWIGGLYTUFF\x10\'\x12\t\n\x05ZUBAT\x10(\x12\n\n\x06GOLBAT\x10)\x12\n\n\x06ODDISH\x10*\x12\t\n\x05GLOOM\x10+\x12\r\n\tVILEPLUME\x10,\x12\t\n\x05PARAS\x10-\x12\x0c\n\x08PARASECT\x10.\x12\x0b\n\x07VENONAT\x10/\x12\x0c\n\x08VENOMOTH\x10\x30\x12\x0b\n\x07\x44IGLETT\x10\x31\x12\x0b\n\x07\x44UGTRIO\x10\x32\x12\n\n\x06MEOWTH\x10\x33\x12\x0b\n\x07PERSIAN\x10\x34\x12\x0b\n\x07PSYDUCK\x10\x35\x12\x0b\n\x07GOLDUCK\x10\x36\x12\n\n\x06MANKEY\x10\x37\x12\x0c\n\x08PRIMEAPE\x10\x38\x12\r\n\tGROWLITHE\x10\x39\x12\x0c\n\x08\x41RCANINE\x10:\x12\x0b\n\x07POLIWAG\x10;\x12\r\n\tPOLIWHIRL\x10<\x12\r\n\tPOLIWRATH\x10=\x12\x08\n\x04\x41\x42RA\x10>\x12\x0b\n\x07KADABRA\x10?\x12\x0c\n\x08\x41LAKAZAM\x10@\x12\n\n\x06MACHOP\x10\x41\x12\x0b\n\x07MACHOKE\x10\x42\x12\x0b\n\x07MACHAMP\x10\x43\x12\x0e\n\nBELLSPROUT\x10\x44\x12\x0e\n\nWEEPINBELL\x10\x45\x12\x0e\n\nVICTREEBEL\x10\x46\x12\r\n\tTENTACOOL\x10G\x12\x0e\n\nTENTACRUEL\x10H\x12\x0b\n\x07GEODUDE\x10I\x12\x0c\n\x08GRAVELER\x10J\x12\t\n\x05GOLEM\x10K\x12\n\n\x06PONYTA\x10L\x12\x0c\n\x08RAPIDASH\x10M\x12\x0c\n\x08SLOWPOKE\x10N\x12\x0b\n\x07SLOWBRO\x10O\x12\r\n\tMAGNEMITE\x10P\x12\x0c\n\x08MAGNETON\x10Q\x12\x0e\n\nFARFETCH_D\x10R\x12\t\n\x05\x44ODUO\x10S\x12\n\n\x06\x44ODRIO\x10T\x12\x08\n\x04SEEL\x10U\x12\x0b\n\x07\x44\x45WGONG\x10V\x12\n\n\x06GRIMER\x10W\x12\x07\n\x03MUK\x10X\x12\x0c\n\x08SHELLDER\x10Y\x12\x0c\n\x08\x43LOYSTER\x10Z\x12\n\n\x06GASTLY\x10[\x12\x0b\n\x07HAUNTER\x10\\\x12\n\n\x06GENGAR\x10]\x12\x08\n\x04ONIX\x10^\x12\x0b\n\x07\x44ROWZEE\x10_\x12\t\n\x05HYPNO\x10`\x12\n\n\x06KRABBY\x10\x61\x12\x0b\n\x07KINGLER\x10\x62\x12\x0b\n\x07VOLTORB\x10\x63\x12\r\n\tELECTRODE\x10\x64\x12\r\n\tEXEGGCUTE\x10\x65\x12\r\n\tEXEGGUTOR\x10\x66\x12\n\n\x06\x43UBONE\x10g\x12\x0b\n\x07MAROWAK\x10h\x12\r\n\tHITMONLEE\x10i\x12\x0e\n\nHITMONCHAN\x10j\x12\r\n\tLICKITUNG\x10k\x12\x0b\n\x07KOFFING\x10l\x12\x0b\n\x07WEEZING\x10m\x12\x0b\n\x07RHYHORN\x10n\x12\n\n\x06RHYDON\x10o\x12\x0b\n\x07\x43HANSEY\x10p\x12\x0b\n\x07TANGELA\x10q\x12\x0e\n\nKANGASKHAN\x10r\x12\n\n\x06HORSEA\x10s\x12\n\n\x06SEADRA\x10t\x12\x0b\n\x07GOLDEEN\x10u\x12\x0b\n\x07SEAKING\x10v\x12\n\n\x06STARYU\x10w\x12\x0b\n\x07STARMIE\x10x\x12\x0b\n\x07MR_MIME\x10y\x12\x0b\n\x07SCYTHER\x10z\x12\x08\n\x04JYNX\x10{\x12\x0e\n\nELECTABUZZ\x10|\x12\n\n\x06MAGMAR\x10}\x12\n\n\x06PINSIR\x10~\x12\n\n\x06TAUROS\x10\x7f\x12\r\n\x08MAGIKARP\x10\x80\x01\x12\r\n\x08GYARADOS\x10\x81\x01\x12\x0b\n\x06LAPRAS\x10\x82\x01\x12\n\n\x05\x44ITTO\x10\x83\x01\x12\n\n\x05\x45\x45VEE\x10\x84\x01\x12\r\n\x08VAPOREON\x10\x85\x01\x12\x0c\n\x07JOLTEON\x10\x86\x01\x12\x0c\n\x07\x46LAREON\x10\x87\x01\x12\x0c\n\x07PORYGON\x10\x88\x01\x12\x0c\n\x07OMANYTE\x10\x89\x01\x12\x0c\n\x07OMASTAR\x10\x8a\x01\x12\x0b\n\x06KABUTO\x10\x8b\x01\x12\r\n\x08KABUTOPS\x10\x8c\x01\x12\x0f\n\nAERODACTYL\x10\x8d\x01\x12\x0c\n\x07SNORLAX\x10\x8e\x01\x12\r\n\x08\x41RTICUNO\x10\x8f\x01\x12\x0b\n\x06ZAPDOS\x10\x90\x01\x12\x0c\n\x07MOLTRES\x10\x91\x01\x12\x0c\n\x07\x44RATINI\x10\x92\x01\x12\x0e\n\tDRAGONAIR\x10\x93\x01\x12\x0e\n\tDRAGONITE\x10\x94\x01\x12\x0b\n\x06MEWTWO\x10\x95\x01\x12\x08\n\x03MEW\x10\x96\x01\x12\x0e\n\tCHIKORITA\x10\x97\x01\x12\x0c\n\x07\x42\x41YLEEF\x10\x98\x01\x12\r\n\x08MEGANIUM\x10\x99\x01\x12\x0e\n\tCYNDAQUIL\x10\x9a\x01\x12\x0c\n\x07QUILAVA\x10\x9b\x01\x12\x0f\n\nTYPHLOSION\x10\x9c\x01\x12\r\n\x08TOTODILE\x10\x9d\x01\x12\r\n\x08\x43ROCONAW\x10\x9e\x01\x12\x0f\n\nFERALIGATR\x10\x9f\x01\x12\x0c\n\x07SENTRET\x10\xa0\x01\x12\x0b\n\x06\x46URRET\x10\xa1\x01\x12\r\n\x08HOOTHOOT\x10\xa2\x01\x12\x0c\n\x07NOCTOWL\x10\xa3\x01\x12\x0b\n\x06LEDYBA\x10\xa4\x01\x12\x0b\n\x06LEDIAN\x10\xa5\x01\x12\r\n\x08SPINARAK\x10\xa6\x01\x12\x0c\n\x07\x41RIADOS\x10\xa7\x01\x12\x0b\n\x06\x43ROBAT\x10\xa8\x01\x12\r\n\x08\x43HINCHOU\x10\xa9\x01\x12\x0c\n\x07LANTURN\x10\xaa\x01\x12\n\n\x05PICHU\x10\xab\x01\x12\x0b\n\x06\x43LEFFA\x10\xac\x01\x12\x0e\n\tIGGLYBUFF\x10\xad\x01\x12\x0b\n\x06TOGEPI\x10\xae\x01\x12\x0c\n\x07TOGETIC\x10\xaf\x01\x12\t\n\x04NATU\x10\xb0\x01\x12\t\n\x04XATU\x10\xb1\x01\x12\x0b\n\x06MAREEP\x10\xb2\x01\x12\x0c\n\x07\x46LAAFFY\x10\xb3\x01\x12\r\n\x08\x41MPHAROS\x10\xb4\x01\x12\x0e\n\tBELLOSSOM\x10\xb5\x01\x12\x0b\n\x06MARILL\x10\xb6\x01\x12\x0e\n\tAZUMARILL\x10\xb7\x01\x12\x0e\n\tSUDOWOODO\x10\xb8\x01\x12\r\n\x08POLITOED\x10\xb9\x01\x12\x0b\n\x06HOPPIP\x10\xba\x01\x12\r\n\x08SKIPLOOM\x10\xbb\x01\x12\r\n\x08JUMPLUFF\x10\xbc\x01\x12\n\n\x05\x41IPOM\x10\xbd\x01\x12\x0c\n\x07SUNKERN\x10\xbe\x01\x12\r\n\x08SUNFLORA\x10\xbf\x01\x12\n\n\x05YANMA\x10\xc0\x01\x12\x0b\n\x06WOOPER\x10\xc1\x01\x12\r\n\x08QUAGSIRE\x10\xc2\x01\x12\x0b\n\x06\x45SPEON\x10\xc3\x01\x12\x0c\n\x07UMBREON\x10\xc4\x01\x12\x0c\n\x07MURKROW\x10\xc5\x01\x12\r\n\x08SLOWKING\x10\xc6\x01\x12\x0f\n\nMISDREAVUS\x10\xc7\x01\x12\n\n\x05UNOWN\x10\xc8\x01\x12\x0e\n\tWOBBUFFET\x10\xc9\x01\x12\x0e\n\tGIRAFARIG\x10\xca\x01\x12\x0b\n\x06PINECO\x10\xcb\x01\x12\x0f\n\nFORRETRESS\x10\xcc\x01\x12\x0e\n\tDUNSPARCE\x10\xcd\x01\x12\x0b\n\x06GLIGAR\x10\xce\x01\x12\x0c\n\x07STEELIX\x10\xcf\x01\x12\r\n\x08SNUBBULL\x10\xd0\x01\x12\r\n\x08GRANBULL\x10\xd1\x01\x12\r\n\x08QWILFISH\x10\xd2\x01\x12\x0b\n\x06SCIZOR\x10\xd3\x01\x12\x0c\n\x07SHUCKLE\x10\xd4\x01\x12\x0e\n\tHERACROSS\x10\xd5\x01\x12\x0c\n\x07SNEASEL\x10\xd6\x01\x12\x0e\n\tTEDDIURSA\x10\xd7\x01\x12\r\n\x08URSARING\x10\xd8\x01\x12\x0b\n\x06SLUGMA\x10\xd9\x01\x12\r\n\x08MAGCARGO\x10\xda\x01\x12\x0b\n\x06SWINUB\x10\xdb\x01\x12\x0e\n\tPILOSWINE\x10\xdc\x01\x12\x0c\n\x07\x43ORSOLA\x10\xdd\x01\x12\r\n\x08REMORAID\x10\xde\x01\x12\x0e\n\tOCTILLERY\x10\xdf\x01\x12\r\n\x08\x44\x45LIBIRD\x10\xe0\x01\x12\x0c\n\x07MANTINE\x10\xe1\x01\x12\r\n\x08SKARMORY\x10\xe2\x01\x12\r\n\x08HOUNDOUR\x10\xe3\x01\x12\r\n\x08HOUNDOOM\x10\xe4\x01\x12\x0c\n\x07KINGDRA\x10\xe5\x01\x12\x0b\n\x06PHANPY\x10\xe6\x01\x12\x0c\n\x07\x44ONPHAN\x10\xe7\x01\x12\r\n\x08PORYGON2\x10\xe8\x01\x12\r\n\x08STANTLER\x10\xe9\x01\x12\r\n\x08SMEARGLE\x10\xea\x01\x12\x0c\n\x07TYROGUE\x10\xeb\x01\x12\x0e\n\tHITMONTOP\x10\xec\x01\x12\r\n\x08SMOOCHUM\x10\xed\x01\x12\x0b\n\x06\x45LEKID\x10\xee\x01\x12\n\n\x05MAGBY\x10\xef\x01\x12\x0c\n\x07MILTANK\x10\xf0\x01\x12\x0c\n\x07\x42LISSEY\x10\xf1\x01\x12\x0b\n\x06RAIKOU\x10\xf2\x01\x12\n\n\x05\x45NTEI\x10\xf3\x01\x12\x0c\n\x07SUICUNE\x10\xf4\x01\x12\r\n\x08LARVITAR\x10\xf5\x01\x12\x0c\n\x07PUPITAR\x10\xf6\x01\x12\x0e\n\tTYRANITAR\x10\xf7\x01\x12\n\n\x05LUGIA\x10\xf8\x01\x12\n\n\x05HO_OH\x10\xf9\x01\x12\x0b\n\x06\x43\x45LEBI\x10\xfa\x01*\xe9\x01\n\x0eItemIdentifier\x12\x10\n\x0cUNKNOWN_ITEM\x10\x00\x12\r\n\tFULL_HEAL\x10&\x12\x0e\n\nMAX_POTION\x10\x0f\x12\x10\n\x0c\x46ULL_RESTORE\x10\x0e\x12\n\n\x06POTION\x10\x12\x12\x10\n\x0cSUPER_POTION\x10\x11\x12\x10\n\x0cHYPER_POTION\x10\x10\x12\x0e\n\nX_ACCURACY\x10!\x12\x0e\n\nGUARD_SPEC\x10)\x12\x0c\n\x08\x44IRE_HIT\x10,\x12\x0c\n\x08X_ATTACK\x10\x31\x12\x0c\n\x08X_DEFEND\x10\x33\x12\x0b\n\x07X_SPEED\x10\x34\x12\r\n\tX_SPECIAL\x10\x35\x62\x06proto3')

_MOVEIDENTIFIER = DESCRIPTOR.enum_types_by_name['MoveIdentifier']
MoveIdentifier = enum_type_wrapper.EnumTypeWrapper(_MOVEIDENTIFIER)
_POKEMONSPECIES = DESCRIPTOR.enum_types_by_name['PokemonSpecies']
PokemonSpecies = enum_type_wrapper.EnumTypeWrapper(_POKEMONSPECIES)
_ITEMIDENTIFIER = DESCRIPTOR.enum_types_by_name['ItemIdentifier']
ItemIdentifier = enum_type_wrapper.EnumTypeWrapper(_ITEMIDENTIFIER)
UNKNOWN_MOVE = 0
POUND = 1
KARATE_CHOP = 2
DOUBLESLAP = 3
COMET_PUNCH = 4
MEGA_PUNCH = 5
PAY_DAY = 6
FIRE_PUNCH = 7
ICE_PUNCH = 8
THUNDERPUNCH = 9
SCRATCH = 10
VICEGRIP = 11
GUILLOTINE = 12
RAZOR_WIND = 13
SWORDS_DANCE = 14
CUT = 15
GUST = 16
WING_ATTACK = 17
WHIRLWIND = 18
FLY = 19
BIND = 20
SLAM = 21
VINE_WHIP = 22
STOMP = 23
DOUBLE_KICK = 24
MEGA_KICK = 25
JUMP_KICK = 26
ROLLING_KICK = 27
SAND_ATTACK = 28
HEADBUTT = 29
HORN_ATTACK = 30
FURY_ATTACK = 31
HORN_DRILL = 32
TACKLE = 33
BODY_SLAM = 34
WRAP = 35
TAKE_DOWN = 36
THRASH = 37
DOUBLE_EDGE = 38
TAIL_WHIP = 39
POISON_STING = 40
TWINEEDLE = 41
PIN_MISSILE = 42
LEER = 43
BITE = 44
GROWL = 45
ROAR = 46
SING = 47
SUPERSONIC = 48
SONICBOOM = 49
DISABLE = 50
ACID = 51
EMBER = 52
FLAMETHROWER = 53
MIST = 54
WATER_GUN = 55
HYDRO_PUMP = 56
SURF = 57
ICE_BEAM = 58
BLIZZARD = 59
PSYBEAM = 60
BUBBLEBEAM = 61
AURORA_BEAM = 62
HYPER_BEAM = 63
PECK = 64
DRILL_PECK = 65
SUBMISSION = 66
LOW_KICK = 67
COUNTER = 68
SEISMIC_TOSS = 69
STRENGTH = 70
ABSORB = 71
MEGA_DRAIN = 72
LEECH_SEED = 73
GROWTH = 74
RAZOR_LEAF = 75
SOLARBEAM = 76
POISONPOWDER = 77
STUN_SPORE = 78
SLEEP_POWDER = 79
PETAL_DANCE = 80
STRING_SHOT = 81
DRAGON_RAGE = 82
FIRE_SPIN = 83
THUNDERSHOCK = 84
THUNDERBOLT = 85
THUNDER_WAVE = 86
THUNDER = 87
ROCK_THROW = 88
EARTHQUAKE = 89
FISSURE = 90
DIG = 91
TOXIC = 92
CONFUSION = 93
PSYCHIC_M = 94
HYPNOSIS = 95
MEDITATE = 96
AGILITY = 97
QUICK_ATTACK = 98
RAGE = 99
TELEPORT = 100
NIGHT_SHADE = 101
MIMIC = 102
SCREECH = 103
DOUBLE_TEAM = 104
RECOVER = 105
HARDEN = 106
MINIMIZE = 107
SMOKESCREEN = 108
CONFUSE_RAY = 109
WITHDRAW = 110
DEFENSE_CURL = 111
BARRIER = 112
LIGHT_SCREEN = 113
HAZE = 114
REFLECT = 115
FOCUS_ENERGY = 116
BIDE = 117
METRONOME = 118
MIRROR_MOVE = 119
SELFDESTRUCT = 120
EGG_BOMB = 121
LICK = 122
SMOG = 123
SLUDGE = 124
BONE_CLUB = 125
FIRE_BLAST = 126
WATERFALL = 127
CLAMP = 128
SWIFT = 129
SKULL_BASH = 130
SPIKE_CANNON = 131
CONSTRICT = 132
AMNESIA = 133
KINESIS = 134
SOFTBOILED = 135
HI_JUMP_KICK = 136
GLARE = 137
DREAM_EATER = 138
POISON_GAS = 139
BARRAGE = 140
LEECH_LIFE = 141
LOVELY_KISS = 142
SKY_ATTACK = 143
TRANSFORM = 144
BUBBLE = 145
DIZZY_PUNCH = 146
SPORE = 147
FLASH = 148
PSYWAVE = 149
SPLASH = 150
ACID_ARMOR = 151
CRABHAMMER = 152
EXPLOSION = 153
FURY_SWIPES = 154
BONEMERANG = 155
REST = 156
ROCK_SLIDE = 157
HYPER_FANG = 158
SHARPEN = 159
CONVERSION = 160
TRI_ATTACK = 161
SUPER_FANG = 162
SLASH = 163
SUBSTITUTE = 164
STRUGGLE = 165
SKETCH = 166
TRIPLE_KICK = 167
THIEF = 168
SPIDER_WEB = 169
MIND_READER = 170
NIGHTMARE = 171
FLAME_WHEEL = 172
SNORE = 173
CURSE = 174
FLAIL = 175
CONVERSION2 = 176
AEROBLAST = 177
COTTON_SPORE = 178
REVERSAL = 179
SPITE = 180
POWDER_SNOW = 181
PROTECT = 182
MACH_PUNCH = 183
SCARY_FACE = 184
FAINT_ATTACK = 185
SWEET_KISS = 186
BELLY_DRUM = 187
SLUDGE_BOMB = 188
MUD_SLAP = 189
OCTAZOOKA = 190
SPIKES = 191
ZAP_CANNON = 192
FORESIGHT = 193
DESTINY_BOND = 194
PERISH_SONG = 195
ICY_WIND = 196
DETECT = 197
BONE_RUSH = 198
LOCK_ON = 199
OUTRAGE = 200
SANDSTORM = 201
GIGA_DRAIN = 202
ENDURE = 203
CHARM = 204
ROLLOUT = 205
FALSE_SWIPE = 206
SWAGGER = 207
MILK_DRINK = 208
SPARK = 209
FURY_CUTTER = 210
STEEL_WING = 211
MEAN_LOOK = 212
ATTRACT = 213
SLEEP_TALK = 214
HEAL_BELL = 215
RETURN = 216
PRESENT = 217
FRUSTRATION = 218
SAFEGUARD = 219
PAIN_SPLIT = 220
SACRED_FIRE = 221
MAGNITUDE = 222
DYNAMICPUNCH = 223
MEGAHORN = 224
DRAGONBREATH = 225
BATON_PASS = 226
ENCORE = 227
PURSUIT = 228
RAPID_SPIN = 229
SWEET_SCENT = 230
IRON_TAIL = 231
METAL_CLAW = 232
VITAL_THROW = 233
MORNING_SUN = 234
SYNTHESIS = 235
MOONLIGHT = 236
HIDDEN_POWER = 237
CROSS_CHOP = 238
TWISTER = 239
RAIN_DANCE = 240
SUNNY_DAY = 241
CRUNCH = 242
MIRROR_COAT = 243
PSYCH_UP = 244
EXTREMESPEED = 245
ANCIENTPOWER = 246
SHADOW_BALL = 247
FUTURE_SIGHT = 248
ROCK_SMASH = 249
WHIRLPOOL = 250
BEAT_UP = 251
BULBASAUR = 0
IVYSAUR = 1
VENUSAUR = 2
CHARMANDER = 3
CHARMELEON = 4
CHARIZARD = 5
SQUIRTLE = 6
WARTORTLE = 7
BLASTOISE = 8
CATERPIE = 9
METAPOD = 10
BUTTERFREE = 11
WEEDLE = 12
KAKUNA = 13
BEEDRILL = 14
PIDGEY = 15
PIDGEOTTO = 16
PIDGEOT = 17
RATTATA = 18
RATICATE = 19
SPEAROW = 20
FEAROW = 21
EKANS = 22
ARBOK = 23
PIKACHU = 24
RAICHU = 25
SANDSHREW = 26
SANDSLASH = 27
NIDORAN_F = 28
NIDORINA = 29
NIDOQUEEN = 30
NIDORAN_M = 31
NIDORINO = 32
NIDOKING = 33
CLEFAIRY = 34
CLEFABLE = 35
VULPIX = 36
NINETALES = 37
JIGGLYPUFF = 38
WIGGLYTUFF = 39
ZUBAT = 40
GOLBAT = 41
ODDISH = 42
GLOOM = 43
VILEPLUME = 44
PARAS = 45
PARASECT = 46
VENONAT = 47
VENOMOTH = 48
DIGLETT = 49
DUGTRIO = 50
MEOWTH = 51
PERSIAN = 52
PSYDUCK = 53
GOLDUCK = 54
MANKEY = 55
PRIMEAPE = 56
GROWLITHE = 57
ARCANINE = 58
POLIWAG = 59
POLIWHIRL = 60
POLIWRATH = 61
ABRA = 62
KADABRA = 63
ALAKAZAM = 64
MACHOP = 65
MACHOKE = 66
MACHAMP = 67
BELLSPROUT = 68
WEEPINBELL = 69
VICTREEBEL = 70
TENTACOOL = 71
TENTACRUEL = 72
GEODUDE = 73
GRAVELER = 74
GOLEM = 75
PONYTA = 76
RAPIDASH = 77
SLOWPOKE = 78
SLOWBRO = 79
MAGNEMITE = 80
MAGNETON = 81
FARFETCH_D = 82
DODUO = 83
DODRIO = 84
SEEL = 85
DEWGONG = 86
GRIMER = 87
MUK = 88
SHELLDER = 89
CLOYSTER = 90
GASTLY = 91
HAUNTER = 92
GENGAR = 93
ONIX = 94
DROWZEE = 95
HYPNO = 96
KRABBY = 97
KINGLER = 98
VOLTORB = 99
ELECTRODE = 100
EXEGGCUTE = 101
EXEGGUTOR = 102
CUBONE = 103
MAROWAK = 104
HITMONLEE = 105
HITMONCHAN = 106
LICKITUNG = 107
KOFFING = 108
WEEZING = 109
RHYHORN = 110
RHYDON = 111
CHANSEY = 112
TANGELA = 113
KANGASKHAN = 114
HORSEA = 115
SEADRA = 116
GOLDEEN = 117
SEAKING = 118
STARYU = 119
STARMIE = 120
MR_MIME = 121
SCYTHER = 122
JYNX = 123
ELECTABUZZ = 124
MAGMAR = 125
PINSIR = 126
TAUROS = 127
MAGIKARP = 128
GYARADOS = 129
LAPRAS = 130
DITTO = 131
EEVEE = 132
VAPOREON = 133
JOLTEON = 134
FLAREON = 135
PORYGON = 136
OMANYTE = 137
OMASTAR = 138
KABUTO = 139
KABUTOPS = 140
AERODACTYL = 141
SNORLAX = 142
ARTICUNO = 143
ZAPDOS = 144
MOLTRES = 145
DRATINI = 146
DRAGONAIR = 147
DRAGONITE = 148
MEWTWO = 149
MEW = 150
CHIKORITA = 151
BAYLEEF = 152
MEGANIUM = 153
CYNDAQUIL = 154
QUILAVA = 155
TYPHLOSION = 156
TOTODILE = 157
CROCONAW = 158
FERALIGATR = 159
SENTRET = 160
FURRET = 161
HOOTHOOT = 162
NOCTOWL = 163
LEDYBA = 164
LEDIAN = 165
SPINARAK = 166
ARIADOS = 167
CROBAT = 168
CHINCHOU = 169
LANTURN = 170
PICHU = 171
CLEFFA = 172
IGGLYBUFF = 173
TOGEPI = 174
TOGETIC = 175
NATU = 176
XATU = 177
MAREEP = 178
FLAAFFY = 179
AMPHAROS = 180
BELLOSSOM = 181
MARILL = 182
AZUMARILL = 183
SUDOWOODO = 184
POLITOED = 185
HOPPIP = 186
SKIPLOOM = 187
JUMPLUFF = 188
AIPOM = 189
SUNKERN = 190
SUNFLORA = 191
YANMA = 192
WOOPER = 193
QUAGSIRE = 194
ESPEON = 195
UMBREON = 196
MURKROW = 197
SLOWKING = 198
MISDREAVUS = 199
UNOWN = 200
WOBBUFFET = 201
GIRAFARIG = 202
PINECO = 203
FORRETRESS = 204
DUNSPARCE = 205
GLIGAR = 206
STEELIX = 207
SNUBBULL = 208
GRANBULL = 209
QWILFISH = 210
SCIZOR = 211
SHUCKLE = 212
HERACROSS = 213
SNEASEL = 214
TEDDIURSA = 215
URSARING = 216
SLUGMA = 217
MAGCARGO = 218
SWINUB = 219
PILOSWINE = 220
CORSOLA = 221
REMORAID = 222
OCTILLERY = 223
DELIBIRD = 224
MANTINE = 225
SKARMORY = 226
HOUNDOUR = 227
HOUNDOOM = 228
KINGDRA = 229
PHANPY = 230
DONPHAN = 231
PORYGON2 = 232
STANTLER = 233
SMEARGLE = 234
TYROGUE = 235
HITMONTOP = 236
SMOOCHUM = 237
ELEKID = 238
MAGBY = 239
MILTANK = 240
BLISSEY = 241
RAIKOU = 242
ENTEI = 243
SUICUNE = 244
LARVITAR = 245
PUPITAR = 246
TYRANITAR = 247
LUGIA = 248
HO_OH = 249
CELEBI = 250
UNKNOWN_ITEM = 0
FULL_HEAL = 38
MAX_POTION = 15
FULL_RESTORE = 14
POTION = 18
SUPER_POTION = 17
HYPER_POTION = 16
X_ACCURACY = 33
GUARD_SPEC = 41
DIRE_HIT = 44
X_ATTACK = 49
X_DEFEND = 51
X_SPEED = 52
X_SPECIAL = 53


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOVEIDENTIFIER._serialized_start=20
  _MOVEIDENTIFIER._serialized_end=3848
  _POKEMONSPECIES._serialized_start=3851
  _POKEMONSPECIES._serialized_end=7328
  _ITEMIDENTIFIER._serialized_start=7331
  _ITEMIDENTIFIER._serialized_end=7564
# @@protoc_insertion_point(module_scope)