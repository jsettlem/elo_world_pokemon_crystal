import os

from protobuf.battle_pb2 import BattleBatch
from utils.files import load_battle_batch, save_battle_batch


def main():
	path = "W:\\elo_world_output\\crystal\\batches\\showdown_command_server5\\"

	files = [path + file for file in os.listdir(path) if file.endswith(".bin.gz")]

	big_batch = BattleBatch()
	for file in files:
		big_batch.battles.extend(load_battle_batch(file).battles)

	save_battle_batch(big_batch, output_dir="./showdown_omega_batch_5.bin", compressed=False)


if __name__ == "__main__":
	main()
