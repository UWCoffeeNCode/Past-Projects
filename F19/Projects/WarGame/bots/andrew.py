from random import choice

from resources.weapons import Weapons
from resources.helpers import get_distance


class Bot:
    """
    A bot to fire anything at anyone but itself
    """

    def action(self, country_status: dict, world_state: dict):
        distances = {}
        for i in world_state["alive_players"]:
            if i != country_status["ID"]:
                distances[i] = get_distance(world_state["countries"], country_status["ID"], i)
        if len(distances) > 0:
            min_dist = min([distances[i] for i in distances])
        else:
            min_dist = 0

        weak_finisher = []
        pickoff = []
        nuke_steal = []
        spam = []

        for i in world_state["alive_players"]:
            if i != country_status["ID"]:
                if world_state["countries"][i]["Health"] <= 10 and world_state["countries"][i]["Health"] > 0:
                    weak_finisher.append((i, Weapons.LASER))
                if world_state["countries"][i]["Nukes"] > 0 or world_state["countries"][i] == min_dist:
                    if self.has_nukes(country_status):
                        pickoff.append((i, Weapons.NUKE))
                    else:
                        pickoff.append((i, Weapons.MISSILE))
                else:
                    spam.append((i, Weapons.MISSILE))

        attackTypes = [weak_finisher, pickoff, nuke_steal, spam]

        for attackType in attackTypes:
            if len(attackType) >= 1:
                attack = choice(attackType)

        # Fire!
        target = attack[0]
        weapon = attack[1]

        return {
            "Weapon": weapon,
            "Target": target
        }

    def has_nukes(self, country_status: dict):
        return country_status["Nukes"] > 0
