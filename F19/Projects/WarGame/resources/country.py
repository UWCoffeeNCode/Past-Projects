import traceback
from copy import deepcopy
from typing import Dict

from resources import weapons


class Country:
    DEFAULT_HEALTH = 100
    DEFAULT_RESOURCES = 100
    NUKE_STOCKPILE = 1

    def __init__(self, player_class):
        self.alive = True
        self.health = self.DEFAULT_HEALTH
        self.resources = self.DEFAULT_RESOURCES
        self.nukes = self.NUKE_STOCKPILE
        self.killer = None  # Attack Event dictionary

        # Each person's bot is stored here
        # We must instantiate each class
        self.player = player_class()

    def get_action(self, world_state: Dict):
        """ Get the action from the player bot
        """

        country_status = self.serialize()

        try:
            action = self.player.action(deepcopy(country_status), deepcopy(world_state))
        except Exception:
            print("Caught exception for", self.name)
            print(traceback.format_exc())
            action = {}

        action["Source"] = self.id
        action = self._do_action(action)

        return action

    def _do_action(self, action: Dict):
        if "Weapon" in action:
            if action["Weapon"] == weapons.Weapons.NUKE:
                action["Success"] = self.nukes > 0

                if action["Success"]:
                    self.nukes -= 1
            else:
                action["Success"] = True

        return action

    def serialize(self):
        country_status = {
            "Alive": self.alive,
            "Health": self.health,
            "ID": self.id,
            "Resources": self.resources,
            "Nukes": self.nukes
        }

        return country_status

    def take_damage(self, action: Dict):
        damage = action["Event"]["Weapon"].value.DAMAGE
        source = action["Event"]["Source"]

        if self.health > 0:
            self.health -= damage

            if self.health <= 0:
                self.health = 0
                self.killer = action["Event"]

    def __repr__(self):
        return self.name + ": " + str(self.serialize())
