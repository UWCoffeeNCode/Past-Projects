#!/usr/bin/python3

import sys
import os
import pygame
import random
import time


from resources.game_logic import GameLogic
from resources.country import Country


pygame.init()
window = pygame.display.set_mode((800, 600))

from visualizer.weapons import ActiveWeapons
from visualizer.countries import Countries
from visualizer.explosions import Explosions


BLACK = pygame.Color(0, 0, 0)
GREY = pygame.Color(120, 120, 120)


nuclearIcon = pygame.image.load("images/nuclear.png").convert_alpha()
pygame.display.set_icon(nuclearIcon)

TITLE_FONT = pygame.font.Font("fonts/OpenSans-Regular.ttf", 24)


class PyGame:
    BATCH = False
    FPS = 60
    WIDTH = 800
    HEIGHT = 600
    TURN_LENGTH = 1

    def __init__(self, window: pygame.Surface):
        self.game = GameLogic()
        self.window = window
        self.clock = pygame.time.Clock()
        self.active_weapons = ActiveWeapons()
        self.explosions = Explosions()
        self.timer = time.time()
        self.end_game = None

        self.countries = Countries(self.game.countries.countries,
                                   self.WIDTH, self.HEIGHT)

    def start(self):
        running = True
        self.turn_surface = TITLE_FONT.render("Round " + str(self.game.turn),
                                              True, GREY)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return 0

            # Refresh screen
            self.window.fill(BLACK)
            self.window.blit(self.turn_surface, (0, 0))

            self.countries.draw(self.window)
            self.explosions.draw(self.window)

            explosions = self.active_weapons.draw(self.window)
            for e in explosions:
                self.explosions.add(*e)

            if time.time() - self.timer > self.TURN_LENGTH * self.game.turn:
                if not self.game.is_finished():
                    self.game.do_turn()
                    self.game.print_events()
                    self.animate_turn()
                    self.turn_surface = TITLE_FONT.render("Round " + str(self.game.turn),
                                                          True, GREY)

                elif not self.end_game:
                    self.end_game = time.time()
                    self.end_game += int(not self.BATCH)

            pygame.display.update()
            self.clock.tick(self.FPS)


            if self.end_game and self.end_game < time.time():
                break


        if self.game.countries.get_alive_count() == 1:
            alive = self.game.countries.get_survivor()
            print(alive, "is the last one standing.")

        else:
            print("There were no survivors.")

        if not self.BATCH:
            self._finish_game()


    def animate_turn(self):
        for event in self.game.events:
            if "Source" in event and "Target" in event and event["Success"]:
                start = self.countries.countries[event["Source"]].inner.center
                end = self.countries.countries[event["Target"]].inner.center

                self.active_weapons.add(start, end, event, self.TURN_LENGTH)

    def _finish_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                    return 0

            self.clock.tick(self.FPS)


if __name__ == "__main__":
    # Set this to True to watch many repeated conflicts
    PyGame.BATCH = False

    Country.verbose = not PyGame.BATCH
    if PyGame.BATCH:
        PyGame.TURN_LENGTH = 0.1

        for i in range(100):
            active_game = PyGame(window)
            active_game.start()
        pygame.quit()

    else:
        active_game = PyGame(window)
        active_game.start()
