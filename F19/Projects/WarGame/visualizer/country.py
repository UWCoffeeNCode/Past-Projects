import pygame
from typing import Tuple


from visualizer.text_rect import TextRect
from visualizer.weapons import AnimatedWeapon


RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
GREY = pygame.Color(120, 120, 120)

SMALL_FONT = pygame.font.Font("fonts/bebas_neue/BebasNeue-Regular.ttf", 20)
MONO_FONT = pygame.font.Font("fonts/bebas_neue/BebasNeue-Regular.ttf", 24)
nuke_image = pygame.image.load("images/nuclear.png").convert_alpha()
nuke_image = pygame.transform.smoothscale(nuke_image, (16, 16))
nuke_rect = nuke_image.get_rect()


class Country:
    SIZE = 50

    FADED_COLOUR = pygame.Color(0, 0, 20)
    BORDER_COLOUR = pygame.Color(20, 20, 160)

    def __init__(self, country, pos: Tuple[int, int]):
        self.country = country

        self.border = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.inner = self.border.inflate(-6, -6)

        display_name = self.country.name
        self.name = TextRect(SMALL_FONT, display_name, GREY)
        self.health_text = TextRect(MONO_FONT, str(self.country.health), RED)
        self.kill_text = TextRect(SMALL_FONT, str(len(self.country.kills)), GREEN)

        self.set_pos(pos)

    def draw(self, window: pygame.Surface):
        if self.country.health:
            colour = self.BORDER_COLOUR
        else:
            colour = self.FADED_COLOUR

        window.fill(colour, self.border)
        window.fill(BLACK, self.inner)

        if self.country.health:
            self.health_text.text = str(self.country.health)
            self.health_text.check_update()

            self.kill_text.text = str(len(self.country.kills))
            self.kill_text.check_update()

            self.name.draw(window)
            self.kill_text.draw(window)
            self.health_text.draw(window)

            # Draw nuke images
            pos = nuke_rect.copy()
            pos.topleft = self.border.midbottom
            for i in range(self.country.nukes):
                window.blit(nuke_image, pos)
                pos.x += pos.width

    def set_pos(self, pos: Tuple[int, int]):
        self.border.center = pos
        self.inner.center = pos

        self.name.rect.midbottom = self.border.midtop
        self.health_text.rect.center = pos
        self.kill_text.rect.midbottom = self.name.rect.midtop
