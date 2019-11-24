import pygame
import random
import time
from typing import Dict, Tuple

from resources import weapons
from visualizer.timer import Timer


class AnimatedWeapon:
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int],
                 event: Dict, turn_length: int):
        self.start, self.end = start, end

        self.rect = pygame.Rect(0, 0, 10, 10)
        self.event = event
        self.turn_length = turn_length
        self.weapon = event["Attack"]["Weapon"]

        self.timer = Timer(self.get_max_time())
        self.trail = Trail(self._get_colour())

    def get_pos(self):
        sx, sy = self.start
        ex, ey = self.end

        delta = self.timer.get_delta()

        x = sx + (ex - sx) * delta
        y = sy + (ey - sy) * delta

        self.rect.center = x, y

    def draw(self, window):
        if time.time() > self.timer.start_time:
            self.get_pos()
            window.fill(self._get_colour(), self.rect)
            self.trail.draw(window, self.rect.center)

    def get_max_time(self):
        return self.weapon.value.SPEED * self.turn_length

    def _get_colour(self):
        return pygame.Color(*self.weapon.value.COLOUR)

    def resize(self, start: Tuple[int, int], end: Tuple[int, int]):
        self.start, self.end = start, end


class Trail:
    COUNT = 5
    INTERVAL = 1/10

    def __init__(self, colour):
        self.colour = colour
        self.last_pos = []
        self.counter = time.time()

    def draw(self, window, new_pos: Tuple[int, int]):
        self._update(new_pos)

        # Draw trail
        if len(self.last_pos) > 1:
            for point in self.last_pos:
                pygame.draw.circle(window, self.colour, point, 2)

    def _update(self, new_pos: Tuple[int, int]):
        now = time.time()
        if self.counter <= now:
            self.counter += self.INTERVAL
            self.last_pos.append(new_pos)

            while len(self.last_pos) > self.COUNT:
                del self.last_pos[0]


class ActiveWeapons:
    def __init__(self):
        self.weapons = []

    def add(self, start: Tuple[int, int], end: Tuple[int, int],
            event: Dict, turn_length: float):
        self.weapons.append(AnimatedWeapon(start, end, event, turn_length))

    def draw(self, window):
        for e in self.weapons[:]:
            e.draw(window)
            if e.timer.is_done():
                self.weapons.remove(e)
