from resources.weapons import Weapons
from resources.helpers import get_distance


class Bot:
    """
    Find the nearest bot that won't soon be killed.
    Use the nuke as soon as possible (so people don't try to steal it)
    Can also predict the future..

    But first priority is to kill smart bot.
    """

    def action(self, country_status: dict, world_state: dict):
        # Fire at...
        status = self.smart_bot_is_alive(world_state)  # It's really annoying
        if status["Alive"]:
            target = status["ID"]

        else:
            target = self.pick_target(country_status["ID"], world_state)

        # Select a weapon
        if self.has_nukes(country_status):
            weapon = Weapons.NUKE
        else:
            weapon = Weapons.MISSILE

        return {
            "Weapon": weapon,
            "Target": target
        }

    @staticmethod
    def get_distances(own_id: int, world_state: dict):
        """
        Return a dictionary mapping country ids to their distance.
        """

        options = Bot.simulate(own_id, world_state)

        distances = {}
        for i in options:
            distances[i] = get_distance(world_state["countries"], own_id, i)

        return distances

    @staticmethod
    def pick_target(own_id: int, world_state: dict):
        """
        Return a country ID
        """

        # If self is the last player- don't do anything
        if len(world_state["alive_players"]) == 1:
            return None

        # Find the nearest bot and return its id as i
        distances = Bot.get_distances(own_id, world_state)
        min_dist = min(distances.values())

        for i, dist in distances.items():
            if dist == min_dist:
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

        # List comprehension to find alive players in future
        new_alive = [i["ID"] for i in world_state["countries"] if world_state["countries"][i["ID"]]["Health"]]

        # Remove self from the list if possible
        if own_id in new_alive:
            new_alive.remove(own_id)

        # Return alive player ids in the future
        return new_alive

    @staticmethod
    def smart_bot_is_alive(world_state):
        # Set c to that of smart bot
        for c in world_state["countries"]:
            if c["Filename"] == "smart_bot":
                break

        result = {}
        result["Alive"] = c["Health"] > 80  # Worth killing
        if result["Alive"]:
            result["ID"] = c["ID"]

        return result
