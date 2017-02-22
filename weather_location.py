# -*- coding: utf-8 -*-

import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key =os.environ['API_KEY']


def get_weather(api_key):
	geolocator = Nominatim()
	location = geolocator.geocode(input("What location? "))
	forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
	return "{} and {}° at {}".format(forecast.summary, forecast.temperature, location.address)

print(get_weather(api_key))