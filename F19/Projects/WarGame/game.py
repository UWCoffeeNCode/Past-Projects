#!/usr/bin/python3

import time

from resources.game_logic import GameLogic


class TextGame:
    def __init__(self):
        self.game = GameLogic()

    def start(self):
        while (self.game.get_alive_count() > 1
               and self.game.turn <= self.game.MAX_TURNS):

            self.game.do_turn()
            self.game.print_events()
            time.sleep(5)

        if self.game.get_alive_count() == 1:
            alive = self.game.get_last_survivor()
            print(self.game.countries[alive].name, "is the last one standing.")

        else:
            print("There were no survivors.")

        print("Hit enter to exit.")
        input()


if __name__ == "__main__":
    active_game = TextGame()
    active_game.start()
