import random

from utils.data import raw_trainer_data, get_player_by_class_id
from utils.hashids import encode_battle, prettify_hashid


def main():
	trainer_list = raw_trainer_data
	run_identifiers = [
		prettify_hashid(encode_battle(player_trainer["class"], player_trainer["instance"], enemy_trainer["class"],
		                              enemy_trainer["instance"], random.randint(0, 255))) for player_trainer in
		trainer_list for enemy_trainer in trainer_list]

	random.shuffle(run_identifiers)

	with open("battles/battle_list.txt", "w") as battle_list:
		battle_list.write("\n".join(run_identifiers))


def showdown():
	trainer_list = raw_trainer_data

	trainer_Red = get_player_by_class_id(63, 1)
	trainer_Blue = get_player_by_class_id(64, 1)
	run_identifiers = [
		prettify_hashid(
			encode_battle(trainer_Red["class"],
			              trainer_Red["instance"], trainer_Blue["class"], trainer_Blue["instance"], i)) for i in
		range(100_001, 1_000_000)]
	with open("battles/showdown_battles_to_run4.txt", 'r') as f1:
		for battle in f1:
			run_identifiers.append(battle.strip())

	random.shuffle(run_identifiers)

	with open("battles/showdown_battles5.txt", "w") as battle_list:
		battle_list.write("\n".join(run_identifiers))


if __name__ == '__main__':
	# main()
	showdown()
