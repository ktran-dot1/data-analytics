# Working with lists and list methods

groceries = ['milk', 'eggs', 'cereal', 'cookies']
print(groceries)

groceries.pop(3) # removes the item at index 3, which is 'cookies'
print(groceries)

groceries.append('meat') # adds 'meat' to the end of the list
groceries.append('vegan alternatives')
print(groceries)

groceries.insert(1, 'bell peppers') # inserts 'bell peppers' at index 1
print(groceries)

print(sorted(groceries)) # prints a sorted version of the list, but does not change the original list

groceries.sort() # sort() method is going to re-sort the list items in place
print(groceries)

groceries.reverse() # reverse() method is going to reverse the order of the list items in place
print(groceries)

print(min(groceries)) # min() function returns the smallest item in the list (alphabetically
print(max(groceries)) # max() function returns the largest item in the list (alphabetically

groc_purchase = [2.99, 6.99, 10.50, 12.99, 4.55]
print(min(groc_purchase))
print(sum(groc_purchase)) # sum() function returns the total of all the items in the list

row_item = '2.99, 6.99, 10.50, 12.99, 4.55'
split_row = row_item.split(', ')
print('After splitting string:',split_row)

row_num = []

for item in split_row:
    row_num.append(float(item)) # convert each string item to a float and add it to the row_num list
print('Using loop to convert strings to floats: ', row_num)

print(sum(row_num)) # now we can use sum() function to get the total of the numbers in the list


# print(sum(row_item)) # this will not work because row_item is a string, not a list of numbers
