import traceback
from typing import Dict


from resources.weapons import Weapons
from resources.helpers import is_valid_action, mydeepcopy


class Country:
    __slots__ = ("alive", "filename", "health", "id", "kills", "name",
                 "resources", "nukes", "killer", "player")
    DEFAULT_HEALTH = 100
    DEFAULT_RESOURCES = 100
    NUKE_STOCKPILE = 0
    verbose = True

    def __init__(self, player_class):
        self.alive = True
        self.health = self.DEFAULT_HEALTH
        self.resources = self.DEFAULT_RESOURCES
        self.nukes = self.NUKE_STOCKPILE
        self.kills = []
        self.killer = None  # Attack Event dictionary

        # Each person's bot is stored here
        # We must instantiate each class
        self.player = player_class()

    def get_action(self, world_state: Dict):
        """ Get the action from the player bot
        """

        action = None
        country_status = self.serialize()

        try:
            attack = self.player.action(country_status, mydeepcopy(world_state))

            if attack:
                attack["Source"] = self.id
                attack = self._do_action(attack)

                action = {
                    "Attack": attack
                }

                assert is_valid_action(action, world_state["alive_players"])

            else:
                action = {}

        except Exception:
            if self.verbose:
                print("Caught exception for", self.name)
                print(traceback.format_exc())

                if action:
                    print("Attempted action:", action)

            return {}

        else:
            return action

    def _do_action(self, action: Dict):
        if "Weapon" in action:
            if action["Weapon"] == Weapons.NUKE:
                action["Success"] = self.nukes > 0

                if action["Success"]:
                    self.nukes -= 1
            else:
                action["Success"] = True

        return action

    def serialize(self):
        country_status = {
            "Alive": self.alive,
            "Filename": self.filename,
            "Health": self.health,
            "ID": self.id,
            "Kills": self.kills,
            "Name": self.name,
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
