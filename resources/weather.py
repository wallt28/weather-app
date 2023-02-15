import requests
from flask import request, jsonify, render_template
from flask_smorest import Blueprint
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
from datetime import datetime
import os


load_dotenv()

blp = Blueprint("weather", "weather", description="Weather")


def get_weather_data(city):
    geolocator = Nominatim(user_agent="weatherapp")
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude
    apikey = os.getenv('API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={apikey}&units=metric"
    r = requests.get(url).json()

    return r

@blp.route('/')
def weather():
    try:
        city_name = 'New York'
        weather_data = get_weather_data(city_name)

        now = datetime.now()
        # Create the "weather" dictionary with the desired information
        weather = {
            "city": city_name,
            "description": weather_data["weather"][0]["description"],
            "icon": weather_data["weather"][0]["icon"],
            "temperature": int(round(weather_data["main"]["temp"], 1)),
            "windspeed": weather_data['wind']['speed'],
            "humidity": weather_data['main']['humidity'],
            "time_now": now.strftime("%a %d %b %H:%M")
        }
        return render_template("weather.html", weather=weather)
    except Exception as e:
        return (
            jsonify(
                {"error": f"Unable to retrieve weather data for {city_name}. {str(e)}"}
            ),
            500,
        )


@blp.route('/', methods=['POST'])
def index_post():
    try:
        new_city = request.form.get('city-name').title()
        weather_data = get_weather_data(new_city)
        now = datetime.now()
        weather = {
            "city": new_city,
            "description": weather_data["weather"][0]["description"],
            "icon": weather_data["weather"][0]["icon"],
            "temperature": int(round(weather_data["main"]["temp"], 1)),
            "windspeed": weather_data['wind']['speed'],
            "humidity": weather_data['main']['humidity'],
            "time_now": now.strftime("%a %d %b %H:%M")
        }
        return render_template("weather.html", weather=weather)
    except:
        return "Error: could not retrieve weather data for that city. Please try again with a different city."






