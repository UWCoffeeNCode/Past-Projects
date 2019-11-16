from math import ceil
from typing import Dict, List


from resources.countries import Countries
from resources import helpers, weapons


class GameLogic:
    MAX_TURNS = 100
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

    def is_finished(self):
        if self.turn > self.MAX_TURNS:
            print("Turn", self.turn, self.countries)
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

            if ("Weapon" in action
                and action["Weapon"] in weapons.Weapons
                and action["Success"]):
                delay = self.get_delay(action)
                self.active_weapons.append({
                    "Delay": ceil(delay),
                    "Event": action
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
                      event["Death"]["Weapon"].name + "!")
                continue


            source = name(event["Source"])

            if "Target" in event:
                target = name(event["Target"])
            else:
                target = None

            if "Weapon" in event:
                weapon_name = event["Weapon"].name
                print(source, "fired a", weapon_name, "at", target)

                if not event["Success"]:
                    print("But they ran out of", weapon_name + "s.")

            else:
                if target:
                    print(source, "decided to wait and stared at", target)
                else:
                    print(source, "decided to wait.")

        print()
