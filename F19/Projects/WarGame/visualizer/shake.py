from math import sin, cos, pi
from random import uniform

BLACK = (0, 0, 0)
TAU = pi * 2


class Shake:
    __slots__ = "angle", "radius", "x", "y"

    def __init__(self):
        self.angle = 0
        self.radius = 0
        self.calculate()

    def calculate(self):
        self.angle %= TAU
        self.x = sin(self.angle) * self.radius
        self.y = cos(self.angle) * self.radius

    # https://gamedev.stackexchange.com/a/47565
    def start(self, radius):
        self.angle = uniform(0, TAU)
        self.radius = radius
        self.calculate()

    def is_active(self):
        return self.radius > 0

    def animate(self, window):
        """
        Copy the screen and replace with black.
        Then blit the copied screen translated by x and y.
        """

        self.radius *= 0.8

        self.angle += (TAU/2 + uniform(-TAU/6, TAU/6))
        self.calculate()

        tempSurface = window.copy()
        window.fill(BLACK)
        window.blit(tempSurface, (self.x, self.y))

        # End screen shake
        if self.radius <= 1:
            self.x = 0
            self.y = 0
            self.radius = 0
