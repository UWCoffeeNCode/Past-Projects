from resources.weapons import Weapons
from random import choice

class Bot:
    """
    Use the nuke as soon as possible
    """

    def action(self, country_status: dict, world_state: dict):

        ## If I have nuke, I attack person with highest health
        if self.has_nukes(country_status):
            weapon = Weapons.NUKE

            target = None
            currmax = 0
            for c in world_state["countries"]:
                if c["ID"] == country_status["ID"]:
                    continue
                if c["Health"] > currmax:
                   currmax = c["Health"]
                   target = c["ID"] 

        ## Else, I use missile at random person
        else:
            weapon = Weapons.MISSILE

            target_choices = world_state["alive_players"]
            target_choices.remove(country_status["ID"])

            # preferably don't battle with ping and bots about to die
            ping_id = -1
            for c in world_state["countries"]:
                if c["Filename"] == "ping_bot":
                    ping_id = c["ID"]
            if (len(target_choices) > 4):
                target_choices.remove(ping_id)

            # Fire!
            if target_choices:
                target = choice(tuple(target_choices))

        return {
            "Weapon": weapon,
            "Target": target
        }

    @staticmethod
    def has_nukes(country_status: dict):
        return country_status["Nukes"] > 0
