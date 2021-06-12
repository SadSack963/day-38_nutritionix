import nutritionix
import sheety


# Google Spreadsheet
# https://docs.google.com/spreadsheets/d/1b1g_IAHQhqCTf3LwyurYX_9LvCySAJVbVuITaes66Wk/edit#gid=0

exercises = nutritionix.get_exercises()

print(exercises)

for item in exercises:
    exercise = item["name"].title()
    duration = item["duration_min"]
    calories = item["nf_calories"]
    sheety.post_new_row(exercise, duration, calories)
