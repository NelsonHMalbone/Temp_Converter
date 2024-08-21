# piggy back to main2.py
# Source https://www.thoughtco.com/convert-kelvin-to-fahrenheit-609234
# this time we will print out the following
# using kelvin conversion for fahreheit
# Remember, Kelvin temperature is not expressed using degrees, just a capital letter K.

user_Unit_input = input("Is this conversion for ('K') Kelvin, ('F') Fahrenheit: ")
user_Temp_input = float(input("Enter Temperture to convert: "))

if user_Unit_input == "K":
    user_Temp_input = round(9 / 5 * (user_Temp_input - 273) + 32, 2)
    print(f'The temperature in Fahrenheit is: {user_Temp_input}°F')
elif user_Unit_input == "F":
    user_Temp_input = round(5 / 9 * (user_Temp_input - 32) + 273.15)
    print(f'The temperature in Kelvin is: {user_Temp_input} K')
    # This is basically the same as saying Kelvin equals the Celsius value plus 273.15.
else:
    print(f'The {user_Unit_input} is not valid please try again. ')