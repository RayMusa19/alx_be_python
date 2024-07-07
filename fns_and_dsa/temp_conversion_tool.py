global FAHRENHEIT_TO_CELSIUS_FACTOR
global CELSIUS_TO_FAHRENHEIT_FACTOR

temperature = (input('Enter the temperature to convert: '))
unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')

fahrenheit = 0
celsius = 0


if unit == 'F':
    fahrenheit = temperature

elif unit == 'C':
    celsius  = temperature


try:
    temperature = float(temperature)
except ValueError:
    temperature = str(temperature)

if isinstance(temperature, (int, float)):
    FAHRENHEIT_TO_CELSIUS_FACTOR = float((temperature - 32) * (5/9))
    CELSIUS_TO_FAHRENHEIT_FACTOR = float((temperature * (9/5)) + 32)
else:
    FAHRENHEIT_TO_CELSIUS_FACTOR = 'Invalid temperature. Please enter a numeric value.'
    CELSIUS_TO_FAHRENHEIT_FACTOR = 'Invalid temperature. Please enter a numeric value.'




def convert_to_celsius(fahrenheit):
    if isinstance (FAHRENHEIT_TO_CELSIUS_FACTOR, float):
        print(fahrenheit, '°F is', end =' ')
        print(FAHRENHEIT_TO_CELSIUS_FACTOR, '°C')
    else:
        print(FAHRENHEIT_TO_CELSIUS_FACTOR)
    return

def convert_to_fahrenheit(celsius):
    if isinstance(CELSIUS_TO_FAHRENHEIT_FACTOR, float):
        print(celsius, '°C is', end =' ')
        print(CELSIUS_TO_FAHRENHEIT_FACTOR, '°F')
    else:
        print(CELSIUS_TO_FAHRENHEIT_FACTOR)
    return




if unit == 'C':
    convert_to_fahrenheit(celsius)
elif unit == 'F':
    convert_to_celsius(fahrenheit)
else:
    try:
        temperature = float(temperature)
    except ValueError:
        temperature = str(temperature)
    if isinstance(temperature, (float, int)):
        print('Invalid unit. Please enter a valid unit.')
    else:
        print('Invalid Temperature and Unit')
    

