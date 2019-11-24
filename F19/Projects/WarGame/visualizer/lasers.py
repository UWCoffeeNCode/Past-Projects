import pygame
import time

from math import atan2, cos, sin, pi, sqrt
from typing import Tuple


from visualizer.timer import Timer


TAU = 2 * pi


def distance(source, target):
    return sqrt((source[0] - target[0])**2 + (source[1] - target[1])**2)


class Laser:
    COLOUR = pygame.Color("Yellow")

    def __init__(self, source: Tuple[int, int], target: Tuple[int, int],
                 turn_length: float):
        self.source = source

        self.timer = Timer(turn_length / 2)
        self.dist = distance(source, target)
        self.angle = atan2(target[1] - source[1], target[0] - source[0])

    def draw(self, window, FPS):
        delta = self.timer.get_delta()
        full_rot = TAU / 60

        min_angle = self.angle - full_rot / 2
        angle = min_angle + full_rot * delta

        dx = self.dist * cos(angle)
        dy = self.dist * sin(angle)

        target_pos = (
            self.source[0] + dx,
            self.source[1] + dy
        )

        pygame.draw.line(window, self.COLOUR, self.source, target_pos)


class Lasers:
    def __init__(self):
        self.lasers = []

    def add(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int],
            turn_length: float):

        self.lasers.append(Laser(start_pos, end_pos, turn_length))

    def draw(self, window, FPS):
        for p in self.lasers[:]:
            p.draw(window, FPS)
            if p.timer.is_done():
                self.lasers.remove(p)
