from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=URL, headers=header)
website = response.text
soup = BeautifulSoup(website, "html.parser")

price_tag = soup.find(name="span", class_="a-price-whole")
price = float(price_tag.getText().split("$")[1])
print(price)

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")


if price<100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="defneliev@gmail.com", password="rifu xtrq zwkj hfxu")
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="unaozlem@gmail.com",
            msg="Subject:Discount\n\n Buy the thing"
        )

