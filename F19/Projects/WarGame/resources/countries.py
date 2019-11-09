from os.path import abspath, dirname
from typing import Dict, List

import importlib
import os

from resources.country import Country
from resources import helpers


class Countries:
    def __init__(self):
        self.countries = get_countries()

        # Initialize ids
        for i, country in enumerate(self.countries):
            country.id = i

    def check_deaths(self, alive_players: List):
        events = []

        # Kill players who died this turn
        for player in alive_players:
            if self.countries[player].health == 0:
                event = self.countries[player].killer
                source = event["Source"]
                self.countries[player].alive = False

                events.append({
                    "Death": event,
                })

                if self.countries[player].nukes:
                    self.countries[source].nukes += self.countries[player].nukes
                    self.countries[player].nukes = 0

        return events

    def get_actions(self, world_state: Dict):
        actions = []
        alive_countries = self.get_alive()

        for i, country in enumerate(self.countries):
            if not country.alive:
                continue

            action = country.get_action(world_state)

            # Check if action is valid
            if helpers.is_valid_action(action, alive_countries):
                actions.append(action)

        return actions

    def get_alive(self):
        """ Returns indexes """
        return [pos for pos, country in enumerate(self.countries) if country.alive]

    def get_alive_count(self):
        """ Returns an integer """
        return sum(country.alive for country in self.countries)

    def get_name(self, country_id: int):
        return self.countries[country_id].name

    def get_survivor(self):
        assert self.get_alive_count() == 1
        return tuple(self.get_alive())[0]

    def serialize_countries(self):
        countries = []
        for country in self.countries:
            countries.append(country.serialize())

        return countries

    def __repr__(self):
        out = [self.countries[c].__repr__() for c in self.get_alive()]

        if out:
            return "\n".join(out)
        else:
            return "[]"


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
        current = Country(bot_class)
        current.name = name
        countries.append(current)

    return countries
