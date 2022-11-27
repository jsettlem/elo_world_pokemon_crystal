import os

# static files
BASE_DIR = os.path.abspath("static_files")
BGB_NAME = "bgb.exe"
BGB_INI_NAME = "bgb.ini"
BGB_PATH = f"{BASE_DIR}/bgb/{BGB_NAME}"
BGB_INI_PATH = f"{BASE_DIR}/bgb/{BGB_INI_NAME}"
ROM_NAME = "pokecrystal11.gbc"
MEMORY_MAP_NAME = "pokecrystal11.sym"
CHEAT_NAME = "pokecrystal11.cht"
ROM_IMAGE = f"{BASE_DIR}/{ROM_NAME}"
MEMORY_MAP = f"{BASE_DIR}/{MEMORY_MAP_NAME}"
EXP_CHEAT = f"{BASE_DIR}/disable_exp.cht"
CAL_PATCH = f"{BASE_DIR}/fix_cal.cht"
BASE_SAVE = f"{BASE_DIR}/base_state_1.sna"
BASE_AI_SAVE = f"{BASE_DIR}/base_ai_state.sna"
BASE_SWITCH_SAVE = f"{BASE_DIR}/ai_switch_base.sna"
AI_DEMO = f"{BASE_DIR}/ai_demo.dem"

# dynamic files
OUT_SAVE = "outstate.sn1"
AI_INPUT_SAVE = "ai_input.sn1"
AI_OUTPUT_SAVE = "ai_output.sn1"
BATTLE_SAVE = "battlestate.sn1"
OUT_DEMO = "outdemo.dem"

OUT_DIR = "W:/elo_world_output/crystal/"
# SCRATCH_DIR = "W:/elo_world_scratch/crystal/"
SCRATCH_DIR = "R:/"
