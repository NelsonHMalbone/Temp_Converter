# piggy back to main.py
# this time we will print out the following
# using kelvin conversion

user_Unit_Input = input("Is this conversion for ('K') Kelvin, ('C') Celsius: ")
user_Temp_Input = float(input("Enter Temperature to Convert: "))

if user_Unit_Input == 'K':
    user_Temp_Input = round(user_Temp_Input - 273.15, 2)
    print(f'The temperature in Celsius is: {user_Temp_Input}°C')
elif user_Unit_Input == 'C':
    pass
else:
    print(f'The {user_Unit_Input} is not valid please try again. ')