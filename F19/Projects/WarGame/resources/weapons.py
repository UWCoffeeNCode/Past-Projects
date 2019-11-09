from enum import Enum, unique

"""
Speed is the number of turns to reach most distant opponent.
Colour and explosion size are for the visualizer.
"""


class Laser:
    COLOUR = (255, 255, 0)
    COST = 10
    DAMAGE = 20
    EXPLOSION_SIZE = 3
    SPEED = 0
    REVEAL_CHANCE = 1


class Missile:
    COLOUR = (0, 192, 0)
    COST = 10
    DAMAGE = 20
    EXPLOSION_SIZE = 5
    SPEED = 2
    REVEAL_CHANCE = 0.25


class Nuke:
    COLOUR = (255, 0, 0)
    DAMAGE = 100
    EXPLOSION_SIZE = 14
    SPEED = 2
    REVEAL_CHANCE = 1


@unique
class Weapons(Enum):
    LASER = Laser
    MISSILE = Missile
    NUKE = Nuke
