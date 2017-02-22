# -*- coding: utf-8 -*-

import forecastio
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key =os.environ['API_KEY']
latitude = 34.9810
longitude = -79.2242

def get_weather(latitude, longitude, api_key):
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	return "{} and {}°".format(forecast.summary, forecast.temperature)

print(get_weather(latitude, longitude, api_key))