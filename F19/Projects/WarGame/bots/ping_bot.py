from random import choice
from typing import List


from resources.weapons import Weapons


class Bot:
    """
    If you fire a laser it will fire a laser
    If you nuke it- it'll try too..

    A bot that always fires at the last enemy
    """

    def __init__(self):
        self.last_enemy = None
        self.last_weapon = None

    def action(self, country_status: dict, world_state: dict):
        # Did anyone fire at it
        self.review_events(world_state["events"], country_status["ID"])

        # Fire at a target if there is one
        if self.last_enemy is not None and self.last_weapon is not None:
            action, target = self.last_weapon, self.last_enemy

            return {
                "Weapon": action,
                "Target": target
            }

        return {}

    def review_events(self, events: List[dict], self_id: int):
        for event in events:
            # Search for only events that fire at this bot
            if ("Weapon" in event
                    and event["Weapon"] in Weapons and event["Target"] == self_id):
                self.last_enemy = event["Source"]
                self.last_weapon = event["Weapon"]
                break
