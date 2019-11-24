"""
Speed is the number of turns to reach most distant opponent.
Colour and explosion size are for the visualizer.
Reveal chance is not used.
"""


from enum import Enum, unique
from collections import namedtuple


Weapon = namedtuple("Weapon", ["COLOUR", "COST", "DAMAGE", "EXPLOSION_SIZE",
                               "SPEED", "REVEAL_CHANCE"])


Laser = Weapon(
    COLOUR = (255, 255, 0),
    COST = 10,
    DAMAGE = 5,
    EXPLOSION_SIZE = 3,
    SPEED = 0,
    REVEAL_CHANCE = 1,
)

Missile = Weapon(
    COLOUR = (0, 192, 0),
    COST = 10,
    DAMAGE = 15,
    EXPLOSION_SIZE = 5,
    SPEED = 2,
    REVEAL_CHANCE = 0.25,
)


Nuke = Weapon(
    COLOUR = (255, 0, 0),
    COST=30,
    DAMAGE = 50,
    EXPLOSION_SIZE = 14,
    SPEED = 2,
    REVEAL_CHANCE = 1,
)


@unique
class Weapons(Enum):
    LASER = Laser
    MISSILE = Missile
    NUKE = Nuke
