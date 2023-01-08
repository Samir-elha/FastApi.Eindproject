import requests
from todooo.main import app

def get_weather_data(city):
    weather_api_key = "$API"
    endpoint = f"$TOKENAPI"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error retrieving weather data")

@app.get("/weather/{city}")
def get_weather(city: str):
    weather_data = get_weather_data(city)
    return weather_data
