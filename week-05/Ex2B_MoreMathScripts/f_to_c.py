# Celsius = (Fahrenheit - 32) * 5/9
import math

f = int(input("What temperature in Fahrenheit would you like to convert to Celsius? "))

c = (f - 32) * 5/9

print(f"{f} degrees Fahrenheit is equal to {c:.0f} degrees Celsius.")