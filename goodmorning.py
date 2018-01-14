#!/usr/bin/env python2


# API  : api.openweathermap.org
# Github, PyOWM : https://github.com/csparpa/pyowm


import argparse
import datetime
import time
import sys
import pyowm

# Setting colours:
cyan = "\033[1;36m"
red = "\033[1;31m"
purple ="\033[1;35m"
yellow ="\033[1;33m"
endcol = "\033[0;0m"


# Get weather stats using PyOWM, a Python wrapper around the OpenWeatherMap web API.
owm = pyowm.OWM('a250e65761751e535a205f02a631c7ec')
observation = owm.weather_at_place('Adelaide,AU')
w = observation.get_weather()
windDict = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
windSpeed = windDict['speed']
humid = w.get_humidity()   
tempDict = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
maxTemp = tempDict['temp_max']
temp = tempDict['temp']
tempMin = tempDict['temp_min']

tempReadout = "The weather today looks like: \n" + \
           red + "	Temp: " + endcol + "{} degrees celcius\n".format(temp) + \
           "	  with a max of {}, and a min of {}\n".format(maxTemp,tempMin) + endcol + \
           cyan + "	Wind: " + endcol + "{}\n".format(windSpeed) + \
           yellow + "	Humidity: " + endcol + "{} \n".format(humid)



# Get current date.
today = datetime.date.today()
d = today.strftime("%A, %d %B %Y")

# Get current time.
# 24 hour clock:
localtime   = time.localtime()
timeString  = time.strftime("%H:%M:%S", localtime)
# 12 hour clock:
t = time.strftime("%I:%M:%S %p")



# Setting up argParser
parser = argparse.ArgumentParser(description = "Gives details on the current date, time, and weather")
group = parser.add_mutually_exclusive_group()

group.add_argument("-a", "--all", action = "store_true")

group.add_argument("-d", "--date", action = "store_true")
group.add_argument("-t", "--time", action = "store_true")
group.add_argument("-w", "--weather", action = "store_true")

args = parser.parse_args()

# Setting the complete string to cyan colour, printing the string, then resets the colour.
complete = "Hello!\n" + \
           "Today is " + purple + d + endcol + "\n" + \
           "The time is " + purple + t + "\n" + endcol + \
           tempReadout



if args.all:
	print complete
elif args.date:
 	print "Today's date is " + purple + d + endcol
elif args.time:
 	print "24 hour time - " + purple + timeString + endcol + "\n12 hour time - " + purple + t + endcol
elif args.weather:
	print tempReadout



'''
=== COLOUR CODES ===
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
'''