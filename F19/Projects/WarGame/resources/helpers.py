from math import pi, sin
from typing import List


def get_distance(countries: List, country_one: int, country_two: int):
    difference = abs(country_one - country_two)
    rotation = 2 * pi * difference / len(countries)

    chord_length = sin(rotation / 2)
    return chord_length
