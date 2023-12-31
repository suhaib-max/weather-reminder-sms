import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "57235ac50346d7d3c57810d992ca5b5a"
account_sid = 'your'
auth_token = 'your'

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
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='your',
        body="It 's going to rain today.Remember to take umbrella",
        to='your'
    )
