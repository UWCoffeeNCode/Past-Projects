#!/usr/bin/python3

import time

from resources.game_logic import GameLogic


class TextGame:
    def __init__(self):
        self.game = GameLogic()

    def start(self):
        while not self.game.is_finished():
            self.game.do_turn()
            print(self.game.active_weapons)
            time.sleep(0)

        if self.game.countries.get_alive_count() == 1:
            alive = self.game.countries.get_survivor()
            print(self.game.countries.countries[alive].name, "is the last one standing.")

        else:
            print("There were no survivors.")

        print("Hit enter to exit.")
        input()


if __name__ == "__main__":
    active_game = TextGame()
    active_game.start()
