import pygame
import random
import time
from typing import Dict, Tuple

from resources import weapons


RED = pygame.Color(255, 0, 0)
YELLOW = pygame.Color(255, 255, 0)
GREEN = pygame.Color(0, 255, 0)


class AnimatedWeapon:
    COLORS = {
        weapons.Weapons.LASER: YELLOW,
        weapons.Weapons.MISSILE: GREEN,
        weapons.Weapons.NUKE: RED
    }

    def __init__(self, start: Tuple[int, int], end: Tuple[int, int],
                 event: Dict, turn_length: int):
        self.start, self.end = start, end

        self.rect = pygame.Rect(0, 0, 10, 10)
        self.start_time = time.time()
        self.event = event
        self.weapon = event["Weapon"]
        self.turn_length = turn_length
        self.remove = False

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
            window.fill(self.COLORS[self.weapon], self.rect)

        if time.time() - self.start_time > self.get_max_time():
            self.remove = True

    def get_max_time(self):
        return (self.weapon.value.SPEED + 1) * self.turn_length
