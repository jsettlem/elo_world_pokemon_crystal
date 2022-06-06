import threading
import time
import random
import multiprocessing
from pprint import pprint

from joblib import Parallel, delayed

from battle_x_as_crystal import run_battle_with_trainers
from utils.data import raw_trainer_data


def run_battle(trainers):
	start = time.time()
	battle_log = run_battle_with_trainers(*trainers, random.Random("fun"))
	end = time.time()
	return (end - start), len(battle_log.turns)


def main():
	my_rng = random.Random("elo")

	battle_pool = [(my_rng.choice(raw_trainer_data), my_rng.choice(raw_trainer_data)) for i in range(10_000)]
	max_threads = min(4, multiprocessing.cpu_count())

	bench_results = {}

	for cores in range(1, max_threads + 1):
		battles_to_run = battle_pool[:cores * 5]
		core_results = Parallel(n_jobs=cores)(delayed(run_battle)(battle) for battle in battles_to_run)
		total_time = 0
		total_turns = 0
		pprint(core_results)
		for result in core_results:
			total_time += result[0]
			total_turns += result[1]

		bench_results[cores] = total_time / total_turns

	pprint(bench_results)

if __name__ == '__main__':
	main()