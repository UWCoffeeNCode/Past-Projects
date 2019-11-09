from math import pi, sin
from typing import Dict, List

from resources import weapons


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
            action["Weapon"] in weapons.Weapons,
            action["Target"] in alive_countries
        ))
    except KeyError as e:
        print("KeyError", e)
        return False
