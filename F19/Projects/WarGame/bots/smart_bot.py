from random import choice

from resources.weapons import Weapons


class Bot:
    """
    A bot to fire anything at anyone but itself
    """


    def action(self, country_status: dict, world_state: dict):
        weapon_choices = [1, 2, 3]
        if not self.has_nukes(country_status):
            # If you don't have nukes don't try firing them
            weapon_choices.remove(3)

        # Don't shoot yourself please...
        target_choices = world_state["alive_players"]
        target_choices.remove(country_status["ID"])

        # Fire!
        target = choice(target_choices)
        weapon = choice(weapon_choices)

        return {
            "Action": weapon,
            "Target": target
        }

    def has_nukes(self, country_status):
        return country_status["Nukes"] > 0
