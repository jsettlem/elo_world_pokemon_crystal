import os

# static files
BASE_DIR = os.path.abspath("static_files")
BGB_PATH = f"{BASE_DIR}/bgb/bgb.exe"
ROM_NAME = "pokecrystal11.gbc"
MEMORY_MAP_NAME = "pokecrystal11.sym"
ROM_IMAGE = f"{BASE_DIR}/{ROM_NAME}"
MEMORY_MAP = f"{BASE_DIR}/{MEMORY_MAP_NAME}"
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