from random import choice

from resources.weapons import Weapons


class Bot:
    """
    A bot to fire anything at anyone,
    Including itself..
    """

    def action(self, country_status: dict, world_state: dict):
        weapon = choice(list(Weapons))

        if world_state["alive_players"]:
            target = choice(tuple(world_state["alive_players"]))

            return {
                "Weapon": weapon,
                "Target": target
            }

        return {}
