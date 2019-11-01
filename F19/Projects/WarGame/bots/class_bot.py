from random import choice

from resources.weapons import Weapons


class Bot:
    """
    Bot designed in class.
    Fire a nuke at the adjacent bots.
    Otherwise if there are no adjacent bots fire anywhere else.
    """

    def action(self, country_status: dict, world_state: dict):    
        if self.has_nukes(country_status):
            weapon_choices = [Weapons.NUKE]

        else:
            # If you don't have nukes don't try firing them
            weapon_choices = list(Weapons)
            weapon_choices.remove(Weapons.NUKE)

        target_choices = []

        left = country_status["ID"] - 1
        if left in world_state["alive_players"]:
            target_choices.append(left)

        right = country_status["ID"] + 1
        if right in world_state["alive_players"]:
            target_choices.append(right)

        # We could also use, if not target_choices:
        if len(target_choices) == 0:
            target_choices = world_state["alive_players"]

        # Fire!
        target = choice(tuple(target_choices))
        weapon = choice(weapon_choices)

        return {
            "Weapon": weapon,
            "Target": target
        }

    def has_nukes(self, country_status: dict):
        return country_status["Nukes"] > 0
