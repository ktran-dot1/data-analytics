# using if / else
'''
groceries = ["milk", "eggs", "almond yogurt", "bread"]

pantry = ['banana', 'peanut butter', 'Nutella']

groc_check = input("Check for item on grocery list: ")

if groc_check in groceries:
    print(f"Grocery list contains {groc_check}")
elif groc_check in pantry:
    print(f"already in the pantry")
else:
    print("Not on grocery list")
    groceries.append(groc_check)
    print(f"Added {groc_check} to grocery list")

print(f"Grocery list : {groceries}")

# condtions are read top-down -- as soon as a condition returns true, if/else stops checking the rest of the conditions.
'''
'''
print()
print("Grocery basket cost: ")
grocery_budget = 100

basket = [10, 15, 10, 15, 20, 25]

# if sum(basket) < grocery_budget:
#     print(f"Keep shopping - ${grocery_budget - sum(basket)}")
# elif (grocery_budget - sum(basket)) <= 10:
#     print("Caution: you are close to your budget limit")

if (grocery_budget - sum(basket)) <= 10:
    print("Caution: you are close to your budget limit")
    print(f"Actual remaining budget: ${grocery_budget - sum(basket)} left")
elif sum(basket) < grocery_budget:
    print(f"Keep shopping - ${grocery_budget - sum(basket)} left")
'''

# greeting script
# greeting = input("Enter hi: ")

# print(f'You entered {greeting}')

# if greeting[:2].lower() == "hi": # Added index range and .lower method so that Hi or Hi!! also works
#     print("Hello there!")
# else:
#     print("Rude.")


greeting = input("Hi! (Enter greeting): ")

alt_greetings = {"hi", "hello", "hey", "sup", "yo", "howdy", "greetings"} # set of acceptable greetings we expect others to say

print(f'You entered {greeting}')

greeting = greeting.replace("!", "").replace(",", "").replace(".", "").lower() # removes punctuation and converts to lowercase so that we can compare it to the list of acceptable greetings

if greeting in alt_greetings:
    greet, *_ = alt_greetings # unpacking. *_ is a common convention for "I don't care about the rest of the values in this collection"
    print(greet)
else:
    print("Rude.")