""" 
Lesson 1:
    Eliminating redundancy
"""

def is_less_than_ten_v1(x):
    if x < 10 == True:
        return True
    if x >= 10 == True:
        return False

def is_less_than_ten_v2(x):
    # We simplify this condition
    if x < 10:
        return True
    # We use else here instead
    else:
        return False

def is_less_than_ten_v3(x):
    if x < 10:
        return True
    # We can actually eliminate else since it's redundant
    return False

# We can see that doing "x < 10" in-line is shorter than using our function, making it completely useless
def is_less_than_ten_v4(x):
    # We can directly return the boolean value
    return x < 10:


""" 
Lesson 2:
    Typing Library
    List Comprehension
    Generators
    Tuples
"""
from typing import List, Generator, Tuple


def get_unique_numbers_v1(end: int = 1000) -> List[int]:
    unique_numbers = []
    for n in range(end):
        if "42" in str(n):
            unique_numbers.append(n)
    return unique_numbers

def get_unique_numbers_v2(end: int = 1000) -> List[int]:
    return [n for n in range(end) if "42" in str(n)]

def get_unique_numbers_v3(end: int = 1000) -> Generator[int, None, None]:
    for n in range(end):
        if "42" in str(n):
            yield n

def create_custom_deck_v1(suits: List[str], values: List[str]) -> List[Tuple[str, str]]:
    deck = []
    for suit in suits:
        for value in values:
            if value != "JOKER":
                deck.append((suit, value))

def create_custom_deck_v2(suits: List[str], values: List[str]) -> List[Tuple[str, str]]:
    return [(suit, value) for suit in suits for value in values if value is not "JOKER"]


"""
Lesson 3:
    Exceptions
    Custom Exceptions
    Try/Except/Else/Finally
"""
from datetime import datetime


class InvalidTimeException(Exception):
    pass

class TemperatureException(Exception):
    pass

class TooColdException(TemperatureException):
    pass

class TooHotException(TemperatureException):
    pass

def _change_temperature(temperature: int) -> None:
    if temperature > 25:
        raise TooHotException()
    elif temperature < 15:
        raise TooColdException()
    
def set_thermostat(temperature: int, time: datetime = datetime.now()):
    try:
        _change_temperature(temperature)
        # _change_time(time)
    except TemperatureException:
        _change_temperature(20)
    except InvalidTimeException:
        # _change_time(datetime.now())        


"""
Lesson 4:
    Sets
    Dictionaries
    Array
"""
from typing import List, Dict, Set
from collections import defaultdict
from array import array


def check_enrollment(student_ids: Set[int], target_id: int) -> bool:
    return target_id in student_ids

def get_name_frequency_map_v1(names: List[str]) -> Dict[str, int]:
    name_frequency_map = {}
    for name in names:
        if name in name_frequency_map:
            name_frequency_map[name] += 1
        else:
            name_frequency_map[name] = 1
    return name_frequency_map

def get_name_frequency_map_v1(names: List[str]) -> Dict[str, int]:
    name_frequency_map = defaultdict(int)
    for name in names:
        name_frequency_map[name] += 1
    return name_frequency_map

def get_complementary_dna_sequence(dna_seq: List[str]) -> List[str]:
    complement = array('b')
    for nucleotide in dna_seq:
        if nucleotide == 'a':
            complement.append(ord('t'))
        elif nucleotide == 't':
            complement.append(ord('a'))
        elif nucleotide == 'c':
            complement.append(ord('g'))
        elif nucleotide == 'g':
            complement.append(ord('c'))
        else:
            raise Exception("Invalid DNA sequence provided")
    return complement


"""
Lesson 5:
    'is' versus '=='
    Special Methods
"""

class Poem:
    def __init__(self, text, title=None, author=None):
        self.text = text

        self.title = title
        if title is None:
            self.title = "Untitled"
        
        self.author = author
        if author is None:
            self.author = "Anonymous"

        self.__lines = self.__get_lines()
    
    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.text

    def __get_lines(self):
        """ Splits the poetic text into a list of lines
        """
        return [x for x in self.text.split('\n') if x.strip()]

    def __getitem__(self, index):
        """ Allows lines of the poem to be retrieved like a list
        """
        return self.__lines[index]

if __name__ == '__main__':
    road_not_taken = Poem(
        "Two roads diverged in a yellow wood and ...\nInsert rest of poem",
        "The Road Not Taken",
        "Robert Frost"
    )
    # Do operations with the poem
