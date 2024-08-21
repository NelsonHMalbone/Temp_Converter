# piggy back to main2.py
# this time we will print out the following
# using kelvin conversion for fahreheit

user_Unit_input = input("Is this conversion for ('K') Kelvin, ('F') Fahrenheit: ")
user_Temp_input = float(input("Enter Temperture to convert: "))

if user_Unit_input == "K":
    user_Temp_input = round(9 / 5 * (user_Temp_input - 273) + 32, 2)
    print(f'The temperature in Celsius is: {user_Temp_input}°F')
elif user_Unit_input == "F":
    pass
else:
    print(f'The {user_Unit_input} is not valid please try again. ')