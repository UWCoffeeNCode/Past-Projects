from math import ceil
from os.path import abspath, dirname
from typing import List

import importlib
import os


from resources import country, weapons
from resources import helpers


class GameLogic:
    MAX_TURNS = 30

    def __init__(self):
        self.countries = get_countries()
        self.events = []
        self.active_weapons = []

        # Initialize ids
        for i, country in enumerate(self.countries):
            country.id = i

        self.turn = 1

    def do_turn(self):
        print()
        print("Round", self.turn)
        actions = self._get_actions()
        self.events = []
        self._process_actions(actions)
        self._run_active()
        self.turn += 1

    def get_alive_count(self):
        """ Returns an integer """
        return sum(country.alive for country in self.countries)

    def get_last_survivor(self):
        assert self.get_alive_count() == 1
        return tuple(self.get_alive_countries())[0]

    def get_alive_countries(self):
        """ Returns indexes """
        return [pos for pos, country in enumerate(self.countries) if country.alive]

    def _get_world_state(self):
        return {
            "active_weapons": self.active_weapons,
            "countries": self._serialize_countries(),
            "events": self.events,
            "alive_players": self.get_alive_countries()
        }

    def _get_actions(self):
        actions = []
        world_state = self._get_world_state()

        for i, country in enumerate(self.countries):
            if not country.alive:
                continue

            action = country.get_action(world_state)

            # Check if action is valid
            if self._is_valid_action(action):
                actions.append(action)

        return actions

    def _is_valid_action(self, action: dict):
        try:
            if "Weapon" not in action:
                return True

            return all((
                action["Weapon"] in weapons.Weapons,
                action["Target"] in self.get_alive_countries()
            ))
        except KeyError as e:
            print("KeyError", e)
            return False

    def _serialize_countries(self):
        countries = []
        for country in self.countries:
            countries.append(country.serialize())

        return countries

    def _run_active(self):
        alive = self.get_alive_countries()

        for action in self.active_weapons[:]:
            if action["Delay"] <= 0:
                if action["Event"]["Success"]:
                    c = action["Event"]["Target"]
                    self.countries[c].take_damage(action)

                self.active_weapons.remove(action)

            action["Delay"] -= 1

        # Kill players who died this turn
        for player in alive:
            if self.countries[player].health == 0:
                source = self.countries[player].killer
                self.countries[player].alive = False

                self.events.append({
                    "Death": player,
                    "Source": source
                })

                if self.countries[player].nukes:
                    self.countries[source].nukes += self.countries[player].nukes
                    self.countries[player].nukes = 0

    def _process_actions(self, actions: List[dict]):
        """
        Updates self.active_weapons with weapons being fired
        """

        for action in actions:
            self.events.append(action)
            if not action:
                raise Exception(action)

            if "Weapon" in action and action["Weapon"] in weapons.Weapons:
                delay = self.get_delay(action)
                self.active_weapons.append({
                    "Delay": ceil(delay),
                    "Distance": delay,
                    "Event": action
                })

    def get_delay(self, action: dict):
        source, target = action["Source"], action["Target"]

        chord_length = helpers.get_distance(self.countries, target, source)
        chord_length *= action["Weapon"].value.SPEED

        return chord_length

    def print_events(self):
        def name(id):
            return self.countries[id].name

        for event in self.events:
            source = name(event["Source"])

            if "Target" in event:
                target = name(event["Target"])
            else:
                target = None

            if "Death" in event:
                print(name(event["Death"]), "died because of", source + "!")

            elif "Weapon" not in event:
                if target:
                    print(source, "decided to wait and stared at", target)
                else:
                    print(source, "decided to wait.")

            else:
                weapon_name = event["Weapon"].name.lower()
                print(source, "fired a", weapon_name, "at", target)

                if not event["Success"]:
                    print("But they ran out of", weapon_name + "s.")


def get_bots():
    # Dynamically import bots in bots directory to BOTS dictionary
    BOTS = {}  # A dictionary of bot names to Bot classes
    bots = os.path.join(abspath(dirname(dirname(__file__))), "bots")
    for file in os.listdir(bots):
        if not file.endswith(".py"):
            continue

        name = file.replace(".py", "")
        module = "." + name
        BOTS[name] = importlib.import_module(module, "bots").Bot

    return BOTS


def get_countries():
    BOTS = get_bots()

    countries = []
    for name in BOTS:
        bot_class = BOTS[name]
        current = country.Country(bot_class)
        current.name = name
        countries.append(current)

    return countries
