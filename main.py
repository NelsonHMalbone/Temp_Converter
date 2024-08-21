# Brocode TempConvertor
# youtube link: https://youtu.be/4wGuB3oAKc4?si=seYSW2YglJxpENl8&t=619

# asking current degree of temp
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
# asking for temp
# what this in a float because of numbers in deciminals
temp = float(input("Enter the Temperature: "))


if unit == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f'The temperature in Fahrenheit is: {temp}°F')
elif unit == 'F':
    pass
else:
    print(f"{unit} is not a valid unit of measurement please pick C for celsius or F for fahrenheit")
