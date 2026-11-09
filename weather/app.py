
import os
import requests

from argparse import ArgumentParser
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


def get_weather(city):
    if not API_KEY:
        print("API key not found! Check your .env file")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("\n--- Weather Information ---")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")

    except requests.exceptions.HTTPError as error:
        print("API Error", error)
        print("Response", response.text)

    except requests.exceptions.RequestException as error:
        print("Connection Error", error)


def main():
    parser = ArgumentParser()
    parser.add_argument("city", help="enter city name", type=str)

    args = parser.parse_args()

    get_weather(args.city)


if __name__ == "__main__":
    main()
