from random import choice

from resources.weapons import Weapons


class Bot:
    """
    A bot ready to fire anything at anyone,
    Or nothing at no one..
    """

    def action(self, country_status: dict, world_state: dict):
        weapon = choice(list(Weapons))

        target = choice(world_state["alive_players"])

        return {
            "Weapon": weapon,
            "Target": target
        }
