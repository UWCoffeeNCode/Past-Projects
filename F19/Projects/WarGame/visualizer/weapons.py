import pygame
import random
import time
from typing import Dict, Tuple

from resources import weapons


class AnimatedWeapon:
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int],
                 event: Dict, turn_length: int):
        self.start, self.end = start, end

        self.rect = pygame.Rect(0, 0, 10, 10)
        self.start_time = time.time()
        self.event = event
        self.weapon = event["Weapon"]
        self.turn_length = turn_length
        self.remove = False

        self.trail = Trail(self._get_colour())

    def get_pos(self):
        sx, sy = self.start
        ex, ey = self.end

        delta = (time.time() - self.start_time) / self.get_max_time()

        x = sx + (ex - sx) * delta
        y = sy + (ey - sy) * delta

        self.rect.center = x, y

    def draw(self, window):
        if time.time() > self.start_time:
            self.get_pos()
            window.fill(self._get_colour(), self.rect)
            self.trail.draw(window, self.rect.center)

        if time.time() - self.start_time > self.get_max_time():
            self.remove = True

    def get_max_time(self):
        return (self.weapon.value.SPEED + 1) * self.turn_length

    def _get_colour(self):
        return pygame.Color(*self.weapon.value.COLOUR)


class Trail:
    COUNT = 10
    INTERVAL = 10

    def __init__(self, colour):
        self.colour = colour
        self.last_pos = []
        self.counter = self.INTERVAL

    def draw(self, window, new_pos):
        self._update(new_pos)

        # Draw trail
        if len(self.last_pos) > 1:
            for point in self.last_pos:
                pygame.draw.circle(window, self.colour, point, 2)

    def _update(self, new_pos):
        self.counter -= 1

        if self.counter <= 0:
            self.counter = self.INTERVAL
            self.last_pos.append(new_pos)

            while len(self.last_pos) > self.COUNT:
                del self.last_pos[0]
