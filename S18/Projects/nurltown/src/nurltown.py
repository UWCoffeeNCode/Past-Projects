"""
nulrtown.py
Module containing the insertion point into the Nurltown game, along with configurations and utilities
"""

# Importing external modules.
# Some of the statements have the form 'import [THIS] as [THAT]', which just allows as to use
# a shorter alias (alternate name to target the module) to reduce the amount we have to type
import sys                      # Allows access to information about the computer, its filesystem, etc
import pygame as pg             # The Pygame module
import config as cfg            # The configuration file containing parameters about the game
import entities as ntts         # Module containing the classes for the objects that will populate the game
import random as rd             # Module which has useful functions involving random numbers
import colors                   # Imports variables describing colors

def main():
    """
    This is the entry point in to the Nurltown ecosystem simulator. The function does the following:
    1. Instantiates a Pygame session
    2. Set the game configuration and utilities
    3. Populates the ecosystem with an initial collection of nurlets and food
    4. Continuously runs a loop of updating the states of the game entities and redrawing the game state
    """

    width, height = cfg.GAME_WIDTH, cfg.GAME_HEIGHT     # import the game dimensions from the configuration file

    pg.init()       # initialize the pygame module
    pg.font.init()  # initialize the font library

    # Create a text object to test the game loop
    test_font = pg.font.SysFont('Helvetica', 30)
    test_text = test_font.render('GAME DEVELOPMENT IN PROGRESS...', False, (255, 0, 0))

    # Import background
    bg = pg.image.load("assets/grass_background.jpg")

    screen = pg.display.set_mode((width, height))       # create a display object representing the game screen
    constrain_within_screen = screen_constraint_generator(screen)
    get_random_pos = random_pos_generator(screen)

    nurlets = pg.sprite.Group()
    hostiles = pg.sprite.Group()
    food = pg.sprite.Group()

    nurlet = ntts.Nurlet(width/2, height/2)
    hostile_nurlets = [ntts.HostileNurlet(*get_random_pos()) for x in range(2)]
    jellies = [ntts.Food(*get_random_pos()) for x in range(cfg.MAX_NUM_FOOD)]

    # entity_groups = [food, nurlets, hostiles]
    entity_groups = {
        'food': food,
        'nurlets': nurlets,
        'hostiles': hostiles
    }

    nurlets.add(nurlet)
    hostiles.add(hostile_nurlets)
    food.add(jellies)

    while True:

        # Handle the events that the game instance encounters
        # Events can be mouse movements/clicks, key presses, window resizing, joystick use, etc.
        # You can read more about the supported event types here:
        # https://www.pg.org/docs/ref/event.html
        events = pg.event.get()
        keys_pressed = pg.key.get_pressed()
        for event in events:

            # Quit the game and program when the 'x' button on the window is pressed
            if event.type == pg.QUIT: sys.exit()
            # Adds a quick way to exit the game by press the ';' button
            if event.type == pg.KEYDOWN and event.key == pg.K_SEMICOLON: sys.exit()

        # Clear the screen
        screen.fill(colors.black)
        screen.blit(bg, (0, 0))

        # Update the nurlets
        nurlets.update(food, hostiles, keys_pressed)

        # Update the hostiles
        hostiles.update(food)

        # Replenish food
        num_to_respawn = max(0, cfg.MAX_NUM_FOOD - len(food))
        if num_to_respawn: food.add(ntts.Food(*get_random_pos()))

        # Redraw the entities
        for group in entity_groups.values():
            for sprite in group.sprites():
                constrain_within_screen(sprite)
            group.draw(screen)

        # Display test text
        screen.blit(test_text, (180, 500))

        # Display the health bar
        draw_health_bar(screen, nurlet.hp)

        # Display the score
        draw_score(screen, nurlet.score)

        if nurlet.hp <= 0:
            font = pg.font.SysFont('Marker Felt Wide', 120, True)
            game_over_text = font.render('GAME OVER!', False, colors.red)
            screen.blit(game_over_text, (120, height/2 - 60))

        pg.display.update()

def draw_score(screen, score):
    """
    A function which draws the player score on the screen
    :param screen: A game screen
    :type screen: pygame.Surface
    :param score: The score of the player
    :type cur_hp: int
    """

    # Set up the title text
    font = pg.font.SysFont('Marker Felt Wide', 50, True)
    title = font.render('SCORE', False, colors.white)
    score = font.render(str(score), False, colors.white)

    # Display title
    screen.blit(title, (740, 25))
    screen.blit(score, (740, 60))

def draw_health_bar(screen, cur_hp, max_hp=100):
    """
    A function which draws the health bar with the current HP of the nurlet on the screen
    :param screen: A game screen
    :type screen: pygame.Surface
    :param cur_hp: The current hp of the nurlet
    :type cur_hp: float
    :param max_hp: The maximum hp of the nurlet
    :type max_hp: float
    """

    # Set up variables which define the dimensions of the health bar
    health_bar_pos = (25, 50)
    health_bar_width = 300
    health_bar_height = 50

    cur_hp_width = cur_hp / (max_hp) * health_bar_width

    # Set up the title text
    font = pg.font.SysFont('Marker Felt Wide', 30, True)
    title = font.render('HEALTH', False, colors.white)

    # Display title
    screen.blit(title, (25, 25))

    # Display the background color of the health bar
    pg.draw.rect(screen, colors.red, (*health_bar_pos, health_bar_width, health_bar_height))
    # Display the bar representing the current hp
    pg.draw.rect(screen, colors.green, (*health_bar_pos, cur_hp_width, health_bar_height))




def screen_constraint_generator(screen):
    """
    A generator function which produces a function which accepts a sprite and constraints it within the
    bounds of the supplied pygame.Display object
    :param screen: A game screen
    :type screen: pygame.Surface
    :return: A function which constrains a sprite to be within a game display
    :rtype: function
    """

    def generated_func(sprite):
        """
        A function which contains a supplied sprite to be within a game display
        :param sprite: A game sprite
        :type sprite: pygame.sprite.Sprite
        """
        sprite.rect.clamp_ip(screen.get_rect())

    return generated_func


def random_pos_generator(screen):
    """
    A generator Function which produces a function which returns a random location within the bounds of a supplied screen
    :param screen: A game screen
    :type screen: pygame.Surface
    :return: A function which provides a random location within the bounds of a supplied screen
    :rtype: function
    """

    def generated_func():
        """
        A function which provides a random location within the bounds of a supplied screen
        :return: An (x, y) coordinate within the screen
        :rtype: tuple[int]
        """

        rect = screen.get_rect()
        x = rd.randint(rect.left, rect.width)
        y = rd.randint(rect.top, rect.height)

        return x, y

    return generated_func


# Make sure this always stays at the end of the file
# This code block ensures that the main() function (the entry point to the game) only runs if this script
# file is run directly, and not imported as a module.
if __name__ == "__main__":
    main()
