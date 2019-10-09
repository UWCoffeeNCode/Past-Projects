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
    "countries": [An array of country_status dictionaries]
    "events": [An array of dictionaries]
    "alive_players": [An array of integers corresponding to country IDs]
}


Action
A dictionary containing the following keys
{
    "Action": [An element of the Weapon enum]
    "Target": [A country ID]
}

Event
An Action dictionary with an additional key,
{
    "Source": [The ID of the country that performed the action]
    ...
}

Attack Event
An Event dictionary with an additional key,
{
    "Success": [Did they fire their weapon successfully]
    ...
}
