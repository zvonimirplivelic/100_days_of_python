# 1. Create a greeting for your program.
print("Welcome to Band name generator")
# 2. Ask the user for the city that they grew up in.
city_name = input("Type in name of the city where you grew up:\n")
# 3. Ask the user for the name of a pet.
pet_name = input("What is the name of your pet?\n")
# 4. Combine the name of their city and pet and show them their band name.
band_name = f"{city_name} {pet_name}"
# 5. Make sure the input cursor shows on a new line:
# print(f"Generated name of your band is: " + city_name + " " + pet_name)
print(f"\nGenerated name of your band is: {band_name}")
