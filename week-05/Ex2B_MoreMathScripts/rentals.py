# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?

# Test your script with 38 tourists. Now do some separate calculations to check your
# work:
# a) How much money did your script say you had to charge per person?
# b) If you multiply that out, how much did you collect?
# c) How much were the vans?
# d) Why do you have leftover money?

# Number of tourists
import math


tourist = int(input("Enter the number of tourists: "))

# Number of vans needed
vans_needed = math.ceil(tourist / 15)

# Total cost of renting vans
total_cost = vans_needed * 250 

# Cost per person
cost_per_person = total_cost / tourist

# Output results
print(f"Number of vans needed: {vans_needed}")
print(f"Total cost of renting vans: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# Using 38 toursit as an example:
    # a) Cost per person = $19.74
    # b) Total collected = $750.00
    # c) Total cost of vans = $750.00
    # d) Leftover money is due to rounding the cost per person.

