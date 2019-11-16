#!/usr/bin/python3

import multiprocessing
from collections import Counter

from resources.game_logic import GameLogic
from resources.country import Country


Country.verbose = False  # Don't show error messages


class BatchGame:
    def __init__(self):
        self.game = GameLogic()

    def start(self):
        while not self.game.is_finished():
            self.game.do_turn()

        return self.game.countries.get_survivor()

def show_results(final):
    size = sum(final.values())
    print("%-15s | %--4s | %s" % ("Bot", "Wins", "Perc"))
    for bot, wins in final.most_common():
        perc = str(round(100 * wins / size)) + "%"
        print("%-15s | %--4d | %s" % (bot, wins, perc))

def branch(LOOP_COUNT, queue):
    results = Counter()

    for i in range(LOOP_COUNT):
        active_game = BatchGame()
        survivor = active_game.start()
        results[survivor] += 1

    queue.put(results)

def main(count, procs):
    LOOP_COUNT = 2100 // procs
    queue = multiprocessing.SimpleQueue()

    jobs = []
    for _ in range(procs):
        process = multiprocessing.Process(target=branch, args=(LOOP_COUNT, queue))
        jobs.append(process)

    # Start processes
    for j in jobs:
        j.start()

    # Wait for all processes to finish
    for j in jobs:
        j.join()

    # Combine outputs
    final = Counter()
    for _ in range(procs):
        final += queue.get()

    show_results(final)

if __name__ == "__main__":
    procs = max(1, multiprocessing.cpu_count() - 1)
    main(100, procs)
