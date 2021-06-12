import requests
import datetime as dt
import os
from dotenv import load_dotenv


# https://dashboard.sheety.co/
# https://sheety.co/docs/requests
load_dotenv("E:/Python/EnvironmentVariables/.env")
BEARER = os.getenv("API_Bearer_Sheety")
USERNAME = os.getenv("API_Username_Sheety")
PROJECT = "workoutTracking"
SHEET = "workouts"


def post_new_row(exercise, duration, calories):
    date = dt.datetime.now().strftime("%d/%m/%Y")
    time_iso = dt.datetime.now().time()
    time = ((time_iso.hour + ((time_iso.minute + (time_iso.second / 60.0)) / 60.0)) / 24.0)

    base_url = "https://api.sheety.co"
    endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    url = base_url + endpoint_url

    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }

    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(url=url, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)
    """
    {
      "workout": {
        "date": "12/06/2021",
        "time": 0.7404513888888888,
        "exercise": "Run",
        "duration": 10,
        "calories": 200,
        "id": 28
      }
    }
    """

if __name__ == "__main__":
    post_new_row("Run", 10, 200)
