import forecastio
from geopy.geocoders import Nominatim


def get_weather(api_key, address):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
	return "{} and {}° at {}".format(forecast.summary, forecast.temperature, location)

