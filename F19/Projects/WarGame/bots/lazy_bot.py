from random import choice, randint

from resources.weapons import Weapons


class Bot:
    """
    It fires, sometimes.
    """

    interval = 5
    def __init__(self):
        self.counter = self.interval

    def action(self, country_status: dict, world_state: dict):
        # Don't shoot yourself please...
        target_choices = world_state["alive_players"]
        target_choices.remove(country_status["ID"])

        # Fire at...
        target = choice(target_choices)

        # Select a weapon
        self.counter -= randint(1, 3)
        if self.counter > 0:
            weapon = 0
        else:
            self.counter = self.interval
            weapon = choice((1, 2, 3))


        return {
            "Action": weapon,
            "Target": target
        }

    def has_nukes(self, country_status):
        return country_status["Nukes"] > 0
