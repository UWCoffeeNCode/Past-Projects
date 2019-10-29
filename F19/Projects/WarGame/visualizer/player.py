import pygame
from typing import Tuple


from visualizer.text_rect import TextRect
from visualizer.weapons import AnimatedWeapon


RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
GREY = pygame.Color(120, 120, 120)

SANS_FONT = pygame.font.Font("fonts/OpenSans-Regular.ttf", 14)


class Player:
    HEIGHT = 80
    WIDTH = 80

    BORDER_COLOUR = pygame.Color(0, 0, 100)

    def __init__(self, country, pos: Tuple[int, int]):
        self.country = country
        self.health = country.health

        self.border = pygame.Rect(0, 0, self.HEIGHT, self.WIDTH)
        self.inner = self.border.inflate(-10, -10)

        display_name = self.country.name.replace("_", " ").title()
        self.name = TextRect(SANS_FONT, display_name, GREY)
        self.health_text = TextRect(SANS_FONT, str(self.health), RED)
        self.nuke_text = TextRect(SANS_FONT, str(self.country.nukes), GREEN)

        self.set_pos(pos)

    def draw(self, window: pygame.Surface):
        window.fill(self.BORDER_COLOUR, self.border)
        window.fill(BLACK, self.inner)

        if self.health:
            self.health_text.text = str(object=self.health)
            self.health_text.check_update()

            self.nuke_text.text = str(self.country.nukes)
            self.nuke_text.check_update()

            self.name.draw(window)
            self.nuke_text.draw(window)
            self.health_text.draw(window)

    def set_pos(self, pos):
        self.border.center = pos
        self.inner.center = pos

        self.name.rect.midbottom = self.border.midtop
        self.health_text.rect.midbottom = self.name.rect.midtop
        self.nuke_text.rect.center = pos

    def apply_weapon(self, e: AnimatedWeapon):
        self.take_damage(e.weapon.value.DAMAGE)

    def take_damage(self, damage: int):
        if self.health > 0:
            self.health -= damage

            if self.health <= 0:
                self.health = 0
