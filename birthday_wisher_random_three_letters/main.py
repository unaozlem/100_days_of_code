import datetime as dt
import smtplib
import pandas as pd
import random
import os

MY_EMAIL = "your email"
PASSWORD = "your password"

# Get today's date
now = dt.datetime.now()
month = now.month
day_of_today = now.day

# Turn the date into a tuple
today = (month, day_of_today)

# Read the data and convert to dict
df = pd.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]):row for (index, row) in df.iterrows()}

# Check if today is anybody's birthday.
if today in birthdays_dict:
    input_folder = "./letter_templates/"
    file_name = os.listdir(input_folder)
    random_letter_name = os.path.join(input_folder, random.choice(file_name))
    with open(random_letter_name, "r") as f:
        letter_content = f.read()
    individual_letter = letter_content.replace("[NAME]", birthdays_dict[today]["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_dict[today]["email"],
            msg=f"Subject:Happy Birthday\n\n {individual_letter}"
        )

