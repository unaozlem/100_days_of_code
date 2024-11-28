import requests
from twilio.rest import Client
import os


API_KEY = os.environ.get("OWM_API_KEY") # Key is hidden. You need your own accound key
LATITUTE=52.569592
LONGITUTE=13.403230

account_sid = 'ACd8d43bce2ed1ec0e71521dd0fc7f11bd'
auth_token = os.environ.get("AUTH_TOKEN") # Key is hidden. You need your own accound key

parameters = {
    "lat":LATITUTE,
    "lon":LONGITUTE,
    "appid":API_KEY,
    "cnt": 4,
}

response = requests.get(url= "https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status
data = response.json()

#----------------------- One and easy way of doing it --------------------------
# weather_ids = []
# for item in data['list']:
#     weather_id = item["weather"][0]['id']
#     weather_ids.append(weather_id)
# print(weather_ids)

# for id in weather_ids:
#     if id < 700:
#         print("Grab an umbrella")

#----------------------- Much better way of doing it --------------------------
will_rain = False

for item in data["list"]:
    weather_status = item["weather"][0]['id']
    if int(weather_status) < 700:
        will_rain= True
if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+1811154311709',
        body='Take an umbrella 🌂',
        to='+49 xxxx xxxxx'
        )
    print(message.status)

### You can run this on the cloud (pythonanywhere.com). A few more lines of code needed to run in pythonanywhere.