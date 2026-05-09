# Celsius = (Fahrenheit - 32) * 5/9
import math

cel = int(input("What temperature in Celsius would you like to convert to Fahrenheit? "))

fah = (cel * 9/5) + 32

print(f"{cel} degrees Celsius is equal to {fah:.0f} degrees Fahrenheit.")
