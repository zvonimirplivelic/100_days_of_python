year_input = int(input("Please, enter a year you wish to check:\n"))

if year_input % 4 == 0:
    if year_input % 100 == 0:
        if year_input % 400 == 0:
            print(f"Year {year_input}. is leap year")
        else:
            print("Not leap year")
    else:
        print(f"Year {year_input}. is leap year")
else:
    print("Not leap year")