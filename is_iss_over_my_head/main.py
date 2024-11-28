import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.582200 # Your latitude
MY_LONG = 13.408950 # Your longitude
MY_EMAIL = "your email"
PASSWORD = "your password"

# Check if iss close to your location.
def is_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(MY_LAT-iss_latitude) < 5 and abs(MY_LONG-iss_longitude) < 5:
        return True
    else:
        return False

# Check if it is night/dark
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    if sunset < current_hour < sunrise:
        return True
    else:
        return False

# Check regularly and when it is above you send an email.
while True:
    time.sleep(60)
    if is_near() and is_night():  
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs="xxxx@yahoo.com",
                msg="Subject: Look up! \n\n The iss is above you")


