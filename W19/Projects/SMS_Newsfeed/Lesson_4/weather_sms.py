import requests
from twilio.rest import Client

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

def extract_info_from_json(resp):
    """Extract key information from resp dictionary from OpenWeatherMap

    Given a resp dictionary obtained with requests from OpenWeatherMap, return
    the name of the city, the current temperature, the wind speed and the
    weather description as a tuple.

    Parameters
    ----------
    resp: dict
        Dictionary obtained from processing the JSON response from
        OpenWeatherMap

    Returns
    -------
    city: str
        Name of the city whose weather data is being processed
    temp: int
        The current temperature
    wind_spd: float
        The current wind speed
    desc: str
        Short weather description
    """
    city     = resp['name']
    temp     = resp['main']['temp']
    wind_spd = resp['wind']['speed']
    desc     = resp['weather'][0]['description']
    return city, temp, wind_spd, desc

def send_sms(to_phone_number, msg_body, TWILIO_SID, TWILIO_KEY, from_phone_number='+15555555555'):
    """Send an sms with msg_body to to_phone_number

    Using your Twilio credentials, send an sms with msg_body to to_phone_number.
    The TWILIO_SID, TWILIO_KEY, and from_phone_number are all set parameters
    that can be obtained from the Twilio website.

    Parameters
    ----------
    to_phone_number: str
        The phone number you wish to send a message to written in E.164 format
    msg_body: str
        The string that you want to send to to_phone_number
    TWILIO_SID:
        Your Twilio ID
    TWILIO_KEY: str
        The Twilio key associated with that ID
    from_phone_number: str
        A valid Twilio number assigned under the SID. Must be written in E.164 format

    Returns
    -------
    None
    """
    client = Client(TWILIO_SID, TWILIO_KEY)
    client.messages.create(body=msg_body, from_=from_phone_number, to=to_phone_number)

if __name__ == '__main__':
    TWILIO_SID = 'Your Twilio SID here'
    TWILIO_KEY = 'Your Twilio key here'
    OPENWEATHER_KEY = 'Your OpenWeatherMap key here'

    resp = get_weather_dictionary(OPENWEATHER_KEY)
    city, temp, wind_spd, desc = extract_info_from_json(resp)
    msg_body = "City: {}\nTemp: {} C\nWind Speed: {} m/s\nDesc: {}".format(city,temp,wind_spd,desc)

    to_phone_number = '+15555555555'
    from_phone_number = '+15555555555'

    send_sms(to_phone_number, msg_body, TWILIO_SID, TWILIO_KEY, from_phone_number)
