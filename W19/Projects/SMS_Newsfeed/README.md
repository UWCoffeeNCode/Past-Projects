# SMS Morning Newsfeed Project

Learn how to use Python to collect information from the web and text yourself a daily newsfeed. In this completely beginner friendly project we'll first start out with getting the local weather, but then help you find other info you might want to get for your own custom newsfeed.

## Objective
* Send text messages (sms) using Twilio
* Learn how to use web APIs using the requests library
* Host your code on [PythonAnywhere](https://www.pythonanywhere.com)

## Tools and Technologies
* [Python](https://www.python.org)
* [Twilio](https://www.twilio.com)
* [Requests](http://docs.python-requests.org/en/master/)
* [OpenWeatherMap](https://openweathermap.org/)

## Syllabus
| Lesson # | Week # | Date          | Description                                           |
| -------- | ------ | ------------- | ------------------------------------------------------|
| 1        | 4      | Jan 29        | Introduction to the command line and web technologies |
| 2        | 5      | Feb 5         | Install Python and use requests to get the weather |
| -        | 6      | Feb 12        | [Cancelled due to weather]  |
| -        | 7      | Feb 19        | Reading Week Break: Special Meet-Up Activity!         |
| 3        | 8      | Feb 26        | Use Twilio's API to send your first text with the weather  |
| 4        | 9      | Mar 5         | Set up a daily text message using PythonAnywhere's task schedule |
| 5        | 10     | Mar 12        | Explore other useful APIs to make your newsfeed your own |
| 6        | 11     | Mar 19        | Polish any remaining kinks in your projects, add more feeds |
| -        | 12     | Mar 26        |End of Term event!!!! |

## Summary of material covered so far
We have covered how to use the command line, install Python, get the weather and send a text message.
We then wrap all of that up to run on a server.

The command line stuff can be skipped for now.

1) If you haven't installed Python3 on your computer you should do so now.
  - Mac: Follow the instructions for homebrew in [Lesson 2](Lesson_2/ReadMe.md)
  - Windows: Install [miniconda](https://docs.conda.io/en/latest/miniconda.html). Anytime you see a mention of PowerShell or terminal, you should be using the anaconda prompt instead.

If you don't have preferred code editor, I can recommend something like [Atom](https://www.atom.io) or even [Notepad++](https://notepad-plus-plus.org/). The imporant thing is to get syntax highlighting for Python. You can run code by using the `cd` command to change directories to the directory you are storing your code and then running `python3 <name of your code>.py`

2) You will need to install a couple of python libraries. Inside the anaconda prompt run `pip install requests twilio`. This will install the [Requests](http://docs.python-requests.org/en/master/) library (for getting web pages) and the Twilio API (to send the text messages).

3) You'll need to make a couple of accounts:
  - [OpenWeatherMap](https://www.openweathermap.org) and get your API key. It can take up to an hour fo the key to be activated, so don't worry if it doesn't work right away.
  - [Twilio](https://www.twilio.com). Their service is paid, but you'll get $15 of free credit to try them out. You'll need a cellphone number to validate with them to make sure the service works. You should buy a trial number from them, any number from Ontatio should be fine, since it will all count as local anyways.
  - [PythonAnywhere](https://www.pythonanywhere.com). These are the guys we're going to use to host our code online and schedule to run once a day. Their free tier is all we need.

4) You can then look at the code examples in [Lesson 3](Lesson_3/request_weather.py) and [Lesson 4](Lesson_4/weather_sms.py).
The one in Lesson 3 will fetch a Python dictionary with the weather once you give it a valid OpenWeatherMap API key. The one in Lesson 4 will actually send a text message to a number verfied with your Twilio account.

From here you can just pick up from [Lesson 4](Lesson_4).

Ask questions if you need help or get stuck!!
