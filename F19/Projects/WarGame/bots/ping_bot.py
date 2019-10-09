from random import choice, randint

from resources.weapons import Weapons


class Bot:
    """
    If you fire a laser it will fire a laser
    If you nuke it- don't expect a response

    A bot that always fires at the last enemy
    """

    def __init__(self):
        self.last_enemy = -1
        self.last_weapon = -1


    def action(self, country_status: dict, world_state: dict):
        # Did anyone fire at it
        self.review_events(world_state["events"], country_status["ID"])

        # Fire at a target if there is one
        if self.last_enemy >= 0 and self.last_weapon >= 0:
            action, target = self.last_weapon, self.last_enemy
        else:
            action, target = 0, None

        return {
            "Action": action,
            "Target": target
        }

    def review_events(self, events, self_id):
        for event in events:
            # Search for only events that fire at this bot
            if event["Action"] in range(1, 4) and event["Target"] == self_id:
                self.last_enemy = event["Source"]
                self.last_weapon = event["Action"]
                break
