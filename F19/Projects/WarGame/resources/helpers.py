from copy import deepcopy
from math import pi, sin
from typing import Dict, List
import pickle


from resources.weapons import Weapons


def get_distance(countries: List, country_one: int, country_two: int):
    difference = abs(country_one - country_two)
    rotation = 2 * pi * difference / len(countries)

    chord_length = sin(rotation / 2)
    return chord_length


def is_valid_action(action: Dict, alive_countries: List):
    if "Attack" not in action:
        return False

    attack = action["Attack"]

    try:
        if "Weapon" not in attack:
            return False

        return all((
            attack["Weapon"] in Weapons,
            attack["Target"] in alive_countries
        ))
    except KeyError as e:
        print("KeyError", e)
        return False


def mydeepcopy(obj):
    # https://stackoverflow.com/a/19065623
    try:
        return pickle.loads(pickle.dumps(obj, -1))
    except:
        return deepcopy(obj)
