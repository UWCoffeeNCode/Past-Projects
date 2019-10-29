#!/usr/bin/python3

import math
import sys
import os
import pygame
import random
import time

from resources import weapons
from resources.game_logic import GameLogic

pygame.init()
window = pygame.display.set_mode((800, 600))

from visualizer.explosions import Explosion
from visualizer.player import Player
from visualizer.weapons import AnimatedWeapon


BLACK = pygame.Color(0, 0, 0)
GREY = pygame.Color(120, 120, 120)

TAU = math.pi * 2

nuclearIcon = pygame.image.load("images/nuclear.png").convert_alpha()
pygame.display.set_icon(nuclearIcon)

TITLE_FONT = pygame.font.Font("fonts/OpenSans-Regular.ttf", 24)


class PyGame:
    FPS = 60
    WIDTH = 800
    HEIGHT = 600
    TURN_LENGTH = 3

    def __init__(self, window: pygame.Surface):
        self.game = GameLogic()
        self.window = window
        self.clock = pygame.time.Clock()
        self.active_weapons = []
        self.explosions = []
        self.timer = time.time()
        self.end_game = None

        self.countries = []
        country_count = len(self.game.countries)

        for i, c in enumerate(self.game.countries):
            perc = (math.sin(i * TAU / country_count) / 2 + 1/2)
            x = (0.1 + 0.8 * perc) * self.WIDTH

            perc = (math.cos(i * TAU / country_count) / 2 + 1/2)
            y = (0.1 + 0.8 * perc) * self.HEIGHT

            self.countries.append(Player(c, (x, y)))

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

            # Draw countries
            for c in self.countries:
                c.draw(self.window)

            for e in self.explosions[:]:
                e.draw(self.window)
                if not e.frame:
                    self.explosions.remove(e)

            for e in self.active_weapons[:]:
                e.draw(self.window)
                if e.remove:
                    self.active_weapons.remove(e)
                    self.countries[e.event["Target"]].apply_weapon(e)

                    if e.weapon is weapons.Weapons.NUKE:
                        self.explosions.append(Explosion(e.rect.center, frame=14))
                    elif e.weapon is weapons.Weapons.MISSILE:
                        self.explosions.append(Explosion(e.rect.center, frame=5))

            if time.time() - self.timer > self.TURN_LENGTH * self.game.turn:
                if (self.game.get_alive_count() > 1
                        and self.game.turn <= self.game.MAX_TURNS):

                    self.game.do_turn()
                    self.animate_turn()
                    self.turn_surface = TITLE_FONT.render("Round " + str(self.game.turn),
                                                          True, GREY)

                elif not self.end_game and not self.active_weapons:
                    self.end_game = time.time() + 1

            pygame.display.update()
            self.clock.tick(self.FPS)


            if self.end_game and self.end_game < time.time():
                break


        if self.game.get_alive_count() == 1:
            alive = self.game.get_alive_countries()[0]
            print(self.game.countries[alive].name, "is the last one standing.")

        else:
            print("There were no survivors.")

        input()

    def animate_turn(self):
        for event in self.game.events:
            if "Source" in event and "Target" in event:
                start = self.countries[event["Source"]].inner.center
                end = self.countries[event["Target"]].inner.center

                self.active_weapons.append(AnimatedWeapon(start, end, event,
                                                          self.TURN_LENGTH))


if __name__ == "__main__":
    active_game = PyGame(window)
    active_game.start()
