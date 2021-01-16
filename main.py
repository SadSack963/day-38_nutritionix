import nutritionix
import sheety


exercises = nutritionix.get_exercises()

for item in exercises:
    exercise = item["name"].title()
    duration = item["duration_min"]
    calories = item["nf_calories"]
    sheety.post_new_row(exercise, duration, calories)
