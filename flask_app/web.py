from flask import Flask, render_template, request
import weather
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)

@app.route("/")
def index():
	name=request.values.get('name')
	address = request.values.get('address')
	api_key =os.environ['API_KEY']
	forecast = None 
	if address:
		forecast = weather.get_weather(api_key, address)
	return render_template('index.html', forecast=forecast, name=name)

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
    app.run()