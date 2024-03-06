bill_amount = float(input("Please, enter the bill:\n"))
tip = int(input("Please, enter the percentage which you would like to give:\n"))
people_split = float(input("How many people are splitting the bill:\n"))

tip_percent = tip / 100

total_tip_amount = bill_amount * tip_percent
total_bill = bill_amount + total_tip_amount

bill_per_person = total_bill / people_split

#print(f"Each person should pay: {round(bill_per_person, 2)}€")
print(f"Each person should pay: {bill_per_person:.2f}€")