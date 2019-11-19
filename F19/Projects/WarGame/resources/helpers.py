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
    try:
        if "Weapon" not in action:
            return True

        return all((
            action["Weapon"] in Weapons,
            action["Target"] in alive_countries
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
