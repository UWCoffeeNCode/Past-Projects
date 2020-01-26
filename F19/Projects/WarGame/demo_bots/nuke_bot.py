from resources.weapons import Weapons

class Bot:
    def action(self, country_status: dict, world_state: dict):
        targets = world_state["alive_players"]
        targets.remove(country_status["ID"])
        assert len(targets) == 1

        target = tuple(targets)[0]

        return {
            "Weapon": Weapons.NUKE,
            "Target": target
        }
