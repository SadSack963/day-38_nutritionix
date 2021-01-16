import os
import requests


# https://openai.com/blog/openai-api/

# https://developer.nutritionix.com/docs/v2
API_KEY = os.environ.get("APIKey_nutritionix")
APP_ID = os.environ.get("AppID_nutritionix")

# Attribution Requirement
print("Nutritionix Website: https://www.nutritionix.com/")
print("Nutritionix API:     https://developer.nutritionix.com/docs/v2")

base_url = "https://trackapi.nutritionix.com"


# https://docs.google.com/spreadsheets/d/1b1g_IAHQhqCTf3LwyurYX_9LvCySAJVbVuITaes66Wk/edit#gid=0

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

# Query Exercise Endpoint
exercise_url = "/v2/natural/exercise"

exercise = input("What exercise have you done? : ")

params = {
    "query":          exercise,
    "gender":         "male",
    "weight_kg":      95,
    "height_cm":      180,
    "age":            65,
}

url = base_url + exercise_url
response = requests.post(url=url, headers=headers, json=params)
response.raise_for_status()
print(response.text)


