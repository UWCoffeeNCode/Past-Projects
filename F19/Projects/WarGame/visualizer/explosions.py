import os
import pygame

from typing import Tuple


def load_explosions():
    explosions = []
    path = "images/explosions"

    for i in range(1, 16):
        file = str(i) + ".png"

        file_path = os.path.join(path, file)
        image = pygame.image.load(file_path).convert_alpha()
        rect = image.get_rect()

        explosions.append({
            "Image": image,
            "Rect": rect
        })

    return explosions


class Explosion:
    def __init__(self, pos: Tuple[int, int], frame: int):
        self.pos = pos
        self.frame = frame

    def draw(self, window):
        explosion = explosionImages[self.frame]
        rect = explosion["Rect"]

        x, y = self.pos
        x -= rect.width / 2
        y -= rect.height / 2

        window.blit(explosion["Image"], (x, y))
        self.frame -= 1


explosionImages = load_explosions()
