import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "57235ac50346d7d3c57810d992ca5b5a"

weather_parameter = {
    "lat": 11.127693,
    "lon": 76.044945,
    "appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_parameter)
response.raise_for_status()
weather_data = response.json()
weather_data = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]







