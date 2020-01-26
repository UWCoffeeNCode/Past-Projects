#!/usr/bin/python3

import sys
import os
import pygame
import random
import time


from resources.game_logic import GameLogic
from resources.country import Country
from resources.weapons import Weapons


pygame.init()
DEFAULT_FLAG = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE
SIZE = (800, 600)
window = pygame.display.set_mode(SIZE, DEFAULT_FLAG)

from visualizer.weapons import ActiveWeapons
from visualizer.countries import Countries
from visualizer.explosions import Explosions
from visualizer.lasers import Lasers
from visualizer.particles import Particles
from visualizer.shake import Shake


BLACK = pygame.Color(0, 0, 0)
GUI_COLOUR = pygame.Color(0, 180, 180)


nuclearIcon = pygame.image.load("images/nuclear.png").convert_alpha()
pygame.display.set_icon(nuclearIcon)

TITLE_FONT = pygame.font.Font("fonts/FROSTBITE-Narrow Bold.ttf", 24)


class PyGame:
    BATCH = False
    FPS = 60
    TURN_LENGTH = 1
    frame = 0

    def __init__(self, window: pygame.Surface):
        self.end_game = None
        self.fullscreen = False
        self.window = window

        self.game = GameLogic()
        self.clock = pygame.time.Clock()
        self.active_weapons = ActiveWeapons()
        self.explosions = Explosions()
        self.lasers = Lasers()
        self.particles = Particles()
        self.shake = Shake()
        self.timer = time.time()

        self.countries = Countries(self.game.countries.countries, SIZE)

    def start(self):
        global SIZE

        running = True
        self.turn_surface = TITLE_FONT.render("ROUND " + str(self.game.turn),
                                              True, GUI_COLOUR)

        while running:
            for event in pygame.event.get():
                if PyGame.quit_game(event):
                    running = False
                    pygame.quit()
                    return 1

                elif PyGame.press_f11(event):
                    self.toggle_fullscreen()

                elif event.type == pygame.VIDEORESIZE:
                    SIZE = event.size
                    pygame.display.set_mode(event.size, DEFAULT_FLAG)
                    self.countries.resize(*event.size)

            # Refresh screen
            self.window.fill(BLACK)
            self.explosions.draw(self.window)
            self.window.blit(self.turn_surface, (10, 10))

            self.countries.draw(self.window)
            self.lasers.draw(self.window, self.FPS)
            self.particles.draw(self.window, self.FPS)
            self.active_weapons.draw(self.window)

            if time.time() - self.timer > self.TURN_LENGTH * self.game.turn:
                if not self.game.is_finished():
                    self.game.do_turn()
                    self.game.print_events()
                    self.animate_turn()
                    self.turn_surface = TITLE_FONT.render(f"Round {self.game.turn}",
                                                          True, GUI_COLOUR)

                elif not self.end_game:
                    self.end_game = time.time()

                    if self.BATCH:
                        self.end_game += 3

            if self.shake.is_active():
                self.shake.animate(self.window)

            pygame.display.update()
            self.clock.tick(self.FPS)

            if self.end_game and self.end_game < time.time():
                break

        if self.game.countries.get_alive_count():
            alive = self.game.countries.get_survivor()
            print(f"{alive} is the last one standing.")

        else:
            print("There were no survivors.")

        if self.BATCH:
            return 0
        else:
            return self._finish_game()

    def animate_turn(self):
        for event in self.game.events:
            if "Attack" in event:
                if event["Attack"]["Success"]:
                    start = self.countries.get_pos(event["Attack"]["Source"])
                    end_pos = self.countries.get_pos(event["Attack"]["Target"])

                    if event["Attack"]["Weapon"] == Weapons.LASER:
                        self.lasers.add(start, end_pos, self.TURN_LENGTH)
                    else:
                        self.active_weapons.add(start, end_pos, event, self.TURN_LENGTH)

            elif "Death" in event:
                end_pos = self.countries.get_pos(event["Death"]["Target"])
                self.particles.add(end_pos)

            elif "Hit" in event:
                if event["Hit"]["Weapon"] == Weapons.NUKE:
                    self.shake.start(40)

                pos = self.countries.get_pos(event["Hit"]["Target"])
                self.explosions.add(pos, event["Hit"]["Weapon"])

    def screenshot(self):
        path = os.path.join("screenshots", str(PyGame.frame) + '.png')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        pygame.image.save(self.window, path)
        PyGame.frame += 1

    def _finish_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if PyGame.quit_game(event):
                    running = False
                    pygame.quit()
                    return not PyGame.BATCH

                elif PyGame.press_f11(event):
                    self.toggle_fullscreen()

            self.clock.tick(self.FPS)

    @staticmethod
    def press_f11(event):
        return event.type == pygame.KEYUP and event.key == pygame.K_F11

    @staticmethod
    def quit_game(event):
        return (event.type == pygame.QUIT
                or (event.type == pygame.KEYUP
                    and event.key == pygame.K_ESCAPE))

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen

        if self.fullscreen:
            flag = DEFAULT_FLAG | pygame.FULLSCREEN

        pygame.display.set_mode(SIZE, flag)


if __name__ == "__main__":
    # Set this to True to watch many repeated conflicts
    PyGame.BATCH = True

    # Print error messages if not in batch mode
    Country.verbose = not PyGame.BATCH

    while True:
        active_game = PyGame(window)
        player_quit = active_game.start()

        if player_quit:
            break

    pygame.quit()
