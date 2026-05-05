import math

# Gas prices
price = 3.999
gallons_puchased = 4.31
total = price * gallons_puchased
print()
print(price * gallons_puchased)  # not rounded
print(round(price * gallons_puchased, 2))

print()
# Rounding function: Floor and Ceil
print("Floor rounding:", math.floor(price * gallons_puchased)) # goes to the next lowest number
print("Ceiling rounding:", math.ceil(price * gallons_puchased)) # goes to the next highest number

print()
print("Using floor division: ", (price* gallons_puchased) // 1)

# Use of pi from the math library
# print()
# print(math.pi)

print("Gas bill using format function:", format(price * gallons_puchased, ".2f"))