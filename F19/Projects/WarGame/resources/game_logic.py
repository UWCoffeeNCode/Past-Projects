from math import ceil
from typing import Dict, List


from resources.countries import Countries
from resources import helpers, weapons
from resources.helpers import mydeepcopy


class GameLogic:
    MAX_TURNS = 200
    __slots__ = ('countries', 'events', 'active_weapons', 'turn')

    def __init__(self):
        self.countries = Countries()
        self.events = []
        self.active_weapons = []
        self.turn = 1

    def do_turn(self):
        actions = self._get_actions()
        self.events = []
        self._process_actions(actions)
        self._run_active()
        self.turn += 1

    def import_state(self, world_state):
        self.active_weapons = mydeepcopy(world_state["active_weapons"])
        self.countries.import_state(world_state["countries"])
        self.events = mydeepcopy(world_state["events"])

    def is_finished(self):
        if self.turn > self.MAX_TURNS:
            print("Maximum turn count", self.MAX_TURNS, "reached.")
            print("Turn", self.turn, self.countries.get_survivor())
            return True

        return self.countries.get_alive_count() <= 1 and not self.active_weapons

    def _get_world_state(self):
        return {
            "active_weapons": self.active_weapons,
            "countries": self.countries.serialize_countries(),
            "events": self.events,
            "alive_players": self.countries.get_alive()
        }

    def _get_actions(self):
        world_state = self._get_world_state()
        return self.countries.get_actions(world_state)

    def _run_active(self):
        alive = self.countries.get_alive()

        for action in self.active_weapons[:]:
            if action["Delay"] <= 0:
                if action["Event"]["Success"]:
                    c = action["Event"]["Target"]
                    self.countries.countries[c].take_damage(action)
                    self.events.append({
                        "Hit": action["Event"]
                    })

                self.active_weapons.remove(action)

            action["Delay"] -= 1

        # Kill players who died this turn
        self.events += self.countries.check_deaths(alive)

    def _process_actions(self, actions: List[Dict]):
        """
        Updates self.active_weapons with weapons being fired
        """

        for action in actions:
            self.events.append(action)
            if not action:
                raise Exception(action)

            if "Attack" in action:
                attack = action["Attack"]
                if ("Weapon" in attack
                    and attack["Weapon"] in weapons.Weapons
                    and attack["Success"]):

                    delay = self.get_delay(attack)
                    self.active_weapons.append({
                        "Delay": ceil(delay),
                        "Event": attack
                    })

    def get_delay(self, action: Dict):
        source, target = action["Source"], action["Target"]

        chord_length = helpers.get_distance(self.countries.countries,
                                            target, source)
        chord_length *= action["Weapon"].value.SPEED

        return chord_length

    def print_events(self):
        print("Round", self.turn - 1)

        name = self.countries.get_name

        for event in self.events:
            if "Death" in event:
                print(name(event["Death"]["Target"]), "died because of",
                      name(event["Death"]["Source"]), "using a",
                      f'{event["Death"]["Weapon"].name}!')
                continue

            elif "Hit" in event:
                continue

            elif "Attack" in event:
                attack = event["Attack"]
                source = name(attack["Source"])

                if "Target" in attack:
                    target = name(attack["Target"])
                else:
                    target = None

                if "Weapon" in attack:
                    weapon_name = attack["Weapon"].name
                    print(source, "fired a", weapon_name, "at", target)

                    if not attack["Success"]:
                        print("But they ran out of", f"{weapon_name}s.")

        print()
