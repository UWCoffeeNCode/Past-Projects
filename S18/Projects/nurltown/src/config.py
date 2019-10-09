"""
config.py
Module containing the configurations for the Nurltown ecosystem simulation
These configurations contain global and default parameters that dictate
the setup of the ecosystem and behaviors of the entities within, such as
nurlets, food, and obstacles
"""

# The game dimensions, as it will appear on your screen
GAME_WIDTH = 900
GAME_HEIGHT = 600

# The dimensions of nurlets
NURLET_WIDTH = 50
NURLET_HEIGHT = 50

# The speed at which the nurlets travel (# of pixels/frame)
NURLET_SPEED = 8
NURLET_INVINCIBILITY_DURATION = 30

# The speed at which the hostile nurlets travel (# of pixels/frame)
HOSTILE_NURLET_SPEED = 7
HOSTILE_NURLET_STRENGTH = 10

# The maximum HP of the nurlets
NURLET_MAX_HP = 100

# The maximum angle of deflection from origin during the shuffling animation
NURLET_SHUFFLE_ANGLE = 15

# The maximum number of food entities which can exist at once in the ecosystem
MAX_NUM_FOOD = 2