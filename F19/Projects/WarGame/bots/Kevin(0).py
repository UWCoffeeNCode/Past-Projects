from random import choice

from resources.weapons import Weapons

class Bot:
    def action(self, country_status: dict, world_state: dict):
        weapon_choices = list(Weapons)

        target_choices = world_state["alive_players"]
        target_choices.remove(country_status["ID"])

        target_more_choices = []

        

     
        
        for i in target_choices:
            if world_state["countries"][i]["Health"] <= 90:
                target_more_choices.append(i)
                
                

        

        weapon = choice([Weapons.MISSILE, Weapons.LASER])
        target = choice(target_more_choices)

        return {
            "Weapon": weapon,
            "Target": target
        }

    
