# modify one of the previous scripts to create input options
import math

investment = int(input("How much do you have in your savings account? "))
interest_rate = 0.04

# Using the rule of 72
years_to_double = 72 / (interest_rate * 100)
new_investment = investment * 2
print('Your current savings is', investment)
print('At a', format(interest_rate, ".0%"), 
      'interest rate, your savings account will be worth', 
      format(new_investment, ".2f"), 'in', 
      format(years_to_double,".1f"), 'years.')