import requests
from todooo.app import app

def get_weather_data(city):
    weather_api_key = "1b323313039c99c4df87eb09ce28fdcd"
    endpoint = f"https://api.openweathermap.org/data/2.5/weather?q=W=Eindhoven&appid=1b323313039c99c4df87eb09ce28fdcd"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error retrieving weather data")

@app.get("/weather/{city}")
def get_weather(city: str):
    weather_data = get_weather_data(city)
    return weather_data