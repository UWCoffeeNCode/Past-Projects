import requests

def get_weather_dictionary(api_key, city_id='6176823'):
    """Request the weather from OpenWeatherMap
    
    Request the weather for a city, using its city_id, from OpenWeatherMap 
    using the provided api_key. Process the response object assuming it is
    valid JSON and return a Python dictionary version of that JSON.

    Parameters
    ----------
    api_key: str
        A valid API key for OpenWeatherMap in the form of a string
    city_id: str, optinal
        A number from OpenWeatherMap's city id list passed as a string. 
        Defaults to Waterloo Canada.

    Returns
    -------
    resp: dict
        Processed response from server; interpreted as JSON and turned into a
        Python dictionary.
    """
    payload = {'id': city_id, 'appid': api_key, 'units': 'metric'}
    
    raw_resp = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    resp = raw_resp.json()
    return resp
