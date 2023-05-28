import subprocess
import requests
from pytz import timezone
from datetime import datetime, time, timedelta, date
import os
from astral.sun import sun
from astral import LocationInfo
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Livelycu functions
def set_wallpaper(path, monitor):
    runCommand(['setwp', f'--monitor={monitor}', f'--file={path}'])
    return

def runCommand(args):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.run(['Livelycu'] + args, startupinfo=si)
    return

# Functions to check and record current wallpaper
def get_current_wallpaper():
    try:
        with open('current_wallpaper.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def set_current_wallpaper(wallpaper):
    with open('current_wallpaper.txt', 'w') as f:
        f.write(wallpaper)

# Constants
API_KEY = config['DEFAULT']['API_KEY']
LAT = config['DEFAULT']['LAT']
LON = config['DEFAULT']['LON']
WALLPAPER_DIR = config['DEFAULT']['WALLPAPER_DIR']
TIMEZONE = config['DEFAULT']['TIMEZONE']
LOCAL_TIMEZONE = timezone(TIMEZONE)
UTC_TIMEZONE = timezone('UTC')
MONITORS = [int(monitor.strip()) for monitor in config['DEFAULT']['MONITORS'].split(',')]
CITY = config['DEFAULT']['CITY']
COUNTRY = config['DEFAULT']['COUNTRY']

# Function to get the current real world weather
def get_weather():
    url = f'https://api.openweathermap.org/data/2.5/weather?lat='+LAT+'&lon='+LON+'&appid='+API_KEY
    response = requests.get(url)
    data = response.json()
    return data['weather'][0]['main']

# Get local time
current_time = datetime.now().astimezone(LOCAL_TIMEZONE).time()

# Specify the city and country
city = LocationInfo(CITY, COUNTRY, TIMEZONE, LAT, LON)

# Get sunrise and sunset
s = sun(city.observer, date=datetime.now())
sunrise = s['sunrise']
sunset = s['sunset']

# Convert sunrise and sunset to local time
local_sunrise = sunrise.astimezone(LOCAL_TIMEZONE)
local_sunset = sunset.astimezone(LOCAL_TIMEZONE)

#Get the current weather
weather = get_weather().lower()

# confirm the time of day - categorise
if local_sunrise.time() <= current_time < time(12, 0):
    time_of_day = 'Morning'
elif time(12, 0) <= current_time < local_sunset.time():
    time_of_day = 'Day'
elif local_sunset.time() <= current_time < (datetime.combine(date.today(), local_sunset.time()) + timedelta(hours=1)).time():
    time_of_day = 'Sunset'
elif (datetime.combine(date.today(), local_sunset.time()) + timedelta(hours=1)).time() <= current_time <= (datetime.combine(date.today(), local_sunset.time()) + timedelta(hours=2)).time():
    time_of_day = 'Evening'
elif (datetime.combine(date.today(), local_sunset.time()) + timedelta(hours=2)).time() <= current_time <= time(23,59,59):
    time_of_day = 'Night'
elif time(0,0,0) <= current_time < local_sunrise.time():
    time_of_day = 'Night'

# Match irl weather to video
if 'rain' in weather:
    weather = 'Rain'
elif 'drizzle' in weather:
    weather = 'Rain'
elif 'clear' in weather:
    weather = 'Clear'
elif 'clouds' in weather:
    weather = 'Cloud'
elif 'storm' in weather:
    weather = 'Storm'
elif 'snow' in weather:
    weather = 'Snow'

# format time of day and weather for file path
time_of_day = time_of_day.capitalize()
weather = weather.capitalize()

# determine the correct video file
video_file = os.path.join(WALLPAPER_DIR, f'{time_of_day}_{weather}.mp4')

# Check if the current wallpaper is the same as the new correct video file, if not, change it
'''
I added a .txt file that records the last used wallpaper. My program then checks to see if it is still relevant,
and only changes the wallpaper if the current one is outdated. This is to avoid unnecessary updates, 
because when there is an update, there is a noticeable 'flash' back to the normal static wallpaper and I want to minimise this
'''
current_wallpaper = get_current_wallpaper()
if video_file != current_wallpaper:
    for monitor in MONITORS:
        set_wallpaper(video_file, monitor)

