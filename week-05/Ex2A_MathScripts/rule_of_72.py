# How long it will take for an investment to double at a given interest rate?
import math

investment = 5000
interest_rate = 0.04

# Using the rule of 72
years_to_double = 72 / (interest_rate * 100)
new_investment = investment * 2
print('Your current savings is', investment)
print('At a', format(interest_rate, ".0%"), 'interest rate, your savings account will be worth', format(new_investment, ".2f"), 'in', format(years_to_double,".1f"), 'years.')