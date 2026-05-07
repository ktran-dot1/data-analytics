# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

#Display the results
# print('The total due is ' + str(total_due)) # We don't want any type errors. A str and int 
                                            # type can't be added together. We need to convert the 
                                            # total_due to a string before we can concatenate it with 
                                            # the other string. 

print('Food cost is ' + str(food_cost) + ' and tax is ' + str(tax))
# print('Tip is ' + str(tip))
print('Tip is ' + format(tip, '.2f'))
print('Total due is ' + str(total_due))
