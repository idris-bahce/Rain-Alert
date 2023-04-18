import os

import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
MY_PHONE_NU = os.getenv("MY_PHONE_NU")
api_key = os.getenv("api_key")

parameters = {
    "lat": 42.17,
    "lon": 14.19,
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()

data = response.json()

code = data["weather"][0]["id"]

if code < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It is going to rain today don't forget to take umbrella!",
            from_='+16073605918',
            to=MY_PHONE_NU
        )
    print(message.status)
