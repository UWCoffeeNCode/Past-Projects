from enum import Enum, unique

"""
Speed is the number of turns to reach most distant opponent.
"""


class Laser:
    COLOUR = (255, 255, 0)
    COST = 10
    DAMAGE = 20
    SPEED = 0
    REVEAL_CHANCE = 1


class Missile:
    COLOUR = (0, 192, 0)
    COST = 10
    DAMAGE = 20
    SPEED = 2
    REVEAL_CHANCE = 0.25


class Nuke:
    COLOUR = (255, 0, 0)
    DAMAGE = 100
    SPEED = 2
    REVEAL_CHANCE = 1


@unique
class Weapons(Enum):
    LASER = Laser
    MISSILE = Missile
    NUKE = Nuke
