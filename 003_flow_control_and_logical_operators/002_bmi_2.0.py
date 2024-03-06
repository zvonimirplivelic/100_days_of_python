height = float(input("Please, enter your height in meters e.g.: 1.82:\n"))
weight = int(input("Please, enter your weight in kilograms e.g: 71:\n"))
message = ""
bmi = weight / height ** 2

if bmi <= 18:
    message = "You are underweight"
elif bmi >= 18.5 and bmi <= 24.9:
    message = "Your weight is in healthy range"
elif bmi >= 25 and bmi <= 29.9:
    message = "You are overweight"
elif bmi >= 30 and bmi <= 39.9:
    message = "You are obese"
else:
    message = "You are severely obese"

print(f"Your BMI is: {round(bmi, 2)}\n{message}")
