from resources.weapons import Weapons
from resources.helpers import mydeepcopy
import os
import random


class Bot:
    """
    Attack the healthiest bot in the future
    Use the nuke as soon as possible (so people don't try to steal it)
    Can also predict the future..

    But first priority is to kill smart bot.
    """
    """
    def __init__(self):
        path = os.path.abspath(__file__)
        bots = os.path.dirname(path)

        name = f"kevin{random.randint(0, 100)}.py"
        new_name = os.path.join(bots, name)

        os.rename(path, new_name
    """

    def action(self, country_status: dict, world_state: dict):
        # Fire at...
        has_nukes = self.has_nukes(country_status)
        target = self.pick_target(has_nukes, country_status["ID"], world_state)

        # Select a weapon
        if has_nukes:
            weapon = Weapons.NUKE
        else:
            weapon = Weapons.MISSILE

        return {
            "Weapon": weapon,
            "Target": target
        }

    @staticmethod
    def get_healths(has_nukes: bool, own_id: int, world_state: dict):
        """
        Return a dictionary mapping country ids to their distance.
        """

        future_state = Bot.simulate(own_id, mydeepcopy(world_state))

        healths = {}

        for i in future_state["future_alive"]:
            c = world_state["countries"][i]
            if c["ID"] == own_id:
                continue

            elif c["Filename"] == "ping_bot":
                if has_nukes and not c["Nukes"]:
                    healths[c["ID"]] = 10000  # Massive priority
                    break
                elif len(future_state["future_alive"]) > 2:
                    continue

            healths[c["ID"]] = c["Health"]

        return healths

    @staticmethod
    def pick_target(has_nukes: bool, own_id: int, world_state: dict):
        """
        Return a country ID
        """

        # If self is the last player- don't do anything
        if len(world_state["alive_players"]) == 1:
            return None

        # Find the nearest bot and return its id as i
        healths = Bot.get_healths(has_nukes, own_id, world_state)
        max_health = max(healths.values())

        for i, health in healths.items():
            if health == max_health:
                break

        return i

    @staticmethod
    def has_nukes(country_status: dict):
        return country_status["Nukes"] > 0

    @staticmethod
    def simulate(own_id: int, world_state: dict):
        """
        Simulate health of all bots after all weapons hit.
        """

        # Simulate all weapons reaching target
        for active in world_state["active_weapons"]:
            action = active["Event"]
            damage, target = action["Weapon"].value.DAMAGE, action["Target"]

            world_state["countries"][target]["Health"] -= damage

        new_alive = set()
        for c in world_state["countries"]:
            if c["Health"]:
                new_alive.add(c["ID"])

        world_state["future_alive"] = new_alive

        # Return alive player ids in the future
        return world_state
