Implement a class with an action method which takes the same arguments as shown by sample_bot.py. You will take two arguments country_status and world_state. Return a dictionary (we call the Action) with the following keys.

country_status
A dictionary containing the following keys
{
    "Alive": [A boolean],
    "Health": [A non-negative integer],
    "ID": [A unique integer],              
    "Resources": [A non-negative integer],
    "Nukes": [A non-negative integer]
}

world_state
A dictionary containing the following keys
{
    "active_weapons": [An array of Active Weapon dictionaries]
    "countries": [An array of country_status dictionaries]
    "events": [An array of Event dictionaries]
    "alive_players": [An array of integers corresponding to country IDs]
}


Action
A dictionary containing the following keys. If there is no Weapon key then a bot will do nothing.
{
    "Weapon": [An element of the Weapon enum]
    "Target": [A country ID]
}

Event
An Action dictionary with an additional key,
{
    "Source": [The ID of the country that performed the action]
    ...
}

Death Event
An Event dictionary with an additional key,
{
    "Death": [The ID of a country]
    ...
}

Attack Event
An Event dictionary with an additional key,
{
    "Success": [Did they fire their weapon successfully]
    ...
}

Active Weapon
{
    "Delay": [An integer representing the delay until the weapon hits its target]
    "Event": [An attack event]
}
