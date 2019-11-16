#!/usr/bin/python3

from resources.game_logic import GameLogic


class TextGame:
    __slots__ = ('game',)
    def __init__(self):
        self.game = GameLogic()

    def start(self):
        while not self.game.is_finished():
            self.game.do_turn()
            self.game.print_events()

        if self.game.countries.get_alive_count() == 1:
            alive = self.game.countries.get_survivor()
            print(alive, "is the last one standing.")

        else:
            print("There were no survivors.")

        print("Hit enter to exit.")
        input()


if __name__ == "__main__":
    active_game = TextGame()
    active_game.start()
