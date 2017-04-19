from flask import Flask, render_template, request
import weather
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

## This version can only be run locally and is not meant to be deployed to heroku or a similar service.

app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('address')
	api_key =os.environ['API_KEY']
	forecast = None 
	if address:
		forecast = weather.get_weather(api_key, address)
	name=request.values.get('name')
	return render_template('index.html', name=name,  forecast=forecast)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
    app.run()