import os
import requests
import datetime as dt


# https://dashboard.sheety.co/
# https://sheety.co/docs/requests
BEARER = os.environ.get("API_Bearer_Sheety")
USERNAME = os.environ.get("API_Username_Sheety")
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

