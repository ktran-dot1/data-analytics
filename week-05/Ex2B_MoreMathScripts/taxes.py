# How much is tax withheld from x amount of money? with a tax rate of 23%
import math

monthly_income = int(input("Enter your monthly income: "))

tax_rate = 0.23

tax_withheld = monthly_income * tax_rate

print(f"A monthly income of ${monthly_income} will have ${tax_withheld:.2f} withheld for taxes.")