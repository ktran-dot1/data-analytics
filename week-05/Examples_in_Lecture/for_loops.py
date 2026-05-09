# working with for loops

# for i in 'banana': # iterating through each character in the string 'banana'
#     print(i)

# for i in ['banana', 'apple', 'pear']: # iterating through each element in the list
#     for x in i: # iterating through each character in the string element of the list
#         print(x) # prints each character in the string element of the list on a new line

# for i in range(5, 10, 2): # iterating through a range of numbers from 5 to 9 (step of 2)
#     print(i)

# back to groceries

grocery_list = ['peach', 'apple', 'chocolate chip cookies', 'rotisserie chicken', 'pita']
in_stock = {'pita', 'cake', 'bread', 'peach', 'apple', 'ground beef', 'chocolate chip cookies'}
basket = []

for current_item_in_list in grocery_list:
    if current_item_in_list in in_stock:
        basket.append(current_item_in_list)
    else:
        print(f"Not found: {current_item_in_list}")
        print("Go back and check your list again.")
        break

print(basket)