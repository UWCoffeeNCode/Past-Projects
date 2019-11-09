#!/usr/bin/python3

import math
import sys
import sdl2
import sdl2.ext
import time

from resources import weapons
from resources.game_logic import GameLogic


BLACK = sdl2.ext.Color(0, 0, 0)
DARK_GREY = sdl2.ext.Color(40, 40, 40)
TAU = math.pi * 2

#NUCLEAR_IMAGE = sdl2.ext.load_image("images/")

font = sdl2.ext.FontManager(bg_color=BLACK, color=DARK_GREY, size=20,
                            font_path="fonts/OpenSans-Regular.ttf")


class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def render(self, components):
        sdl2.ext.fill(self.surface, BLACK)

        super().render(components)


class Player:
    HEIGHT = 80
    WIDTH = 80

    BORDER_COLOUR = sdl2.ext.Color(0, 0, 80)

    def __init__(self, world, factory, posx=0, posy=0):
        self.border = sdl2.ext.Entity(world)
        size = self.WIDTH, self.HEIGHT
        self.border.sprite = factory.from_color(self.BORDER_COLOUR, size=size)

        self.inner = sdl2.ext.Entity(world)
        size = self.WIDTH - 10, self.HEIGHT - 10
        self.inner.sprite = factory.from_color(BLACK, size=size)

        self.text = factory.from_text("Ok?", fontmanager=font)

        self.set_pos(posx, posy)

    def set_pos(self, posx, posy):
        x, y = round(posx - self.WIDTH / 2), round(posy - self.WIDTH / 2)
        self.border.sprite.position = x, y
        self.inner.sprite.position = x + 5, y + 5


class TextGame:
    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        self.game = GameLogic()

        sdl2.ext.init()
        self.window = sdl2.ext.Window("War Game",
                                      size=(self.WIDTH, self.HEIGHT))
        self.window.show()

        self.world = sdl2.ext.World()

        self.spriterenderer = SoftwareRenderer(self.window)
        self.world.add_system(self.spriterenderer)

        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

        self.countries = []
        country_count = len(self.game.countries)

        # Load countries
        for i, c in enumerate(self.game.countries):
            perc = (math.sin(i * TAU / country_count) / 2 + 1/2)
            x = (0.1 + 0.8 * perc) * self.WIDTH

            perc = (math.cos(i * TAU / country_count) / 2 + 1/2)
            y = (0.1 + 0.8 * perc) * self.HEIGHT

            self.countries.append(Player(self.world, self.factory, x, y))

    def start(self):
        running = True
        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False
                    break

            self.world.process()
        return 0

        while not self.game.is_finished():
            self.game.do_turn()

        if self.game.countries.get_alive_count() == 1:
            alive = self.game.countries.get_survivor()
            print(self.game.countries[alive].name, "is the last one standing.")

        else:
            print("There were no survivors.")

        print("Hit enter to exit.")
        input()


if __name__ == "__main__":
    active_game = TextGame()
    active_game.start()
