height = float(input("Please, enter your height in meters e.g.: 1.82:\n"))
weight = int(input("Please, enter your weight in kilograms e.g: 71:\n"))
message = ""
bmi = weight / height ** 2

print(f"Your BMI is: {round(bmi, 2)}")

