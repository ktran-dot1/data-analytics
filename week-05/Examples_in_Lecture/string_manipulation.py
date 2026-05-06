# working with string indexing, slicing, splitting, and stripping

emp_id = '007'

emp_name = 'James Bond'

print(emp_id[2]) # prints the 3rd character of emp_id
print(emp_id[-1]) # prints the last character of emp_id

print(emp_name[0:5]) # prints the first 5 characters of emp_name (James)
print(emp_name[-4:]) # prints the last name (Bond)

print(len(emp_name)) # prints the length of emp_name

# splitting a string into a list of substrings
fruits = 'banana, apple, orange'
list_of_fruits = fruits.split()
print(list_of_fruits) # prints ['banana,', 'apple,', 'orange']

staff = "James Bond, Miss Moneypenny, Q"
all_staff = staff.split(", ") # splits the staff based on where the comma and space are

print(all_staff) 

print('11/2/1967'.split('/')) # splits the date into a list of ['11', '2', '1967']


address_book = ['Grandma, 100 Pine Tree Dr, Willobrugh PA', 'Aunt Margret, 55 Whistletop, Pinecone WY']
print(address_book[0].split(', '))

grandma = address_book[0].split(', ')
print(grandma)

# Upper / Lower / Title

print(emp_name)
print(emp_name.upper()) # prints the name in all uppercase letters
print(emp_name.lower()) # prints the name in all lowercase letters
print(emp_name.title()) # prints the name in title case (first letter of each word capitalized)

emp_name2 = 'miSS mONEYpENNY'
print(emp_name2.title())

# Using Replace
print('$1,250.00'.replace('$', '')) # removes the $ from the string

gma_addr = 'Grandma, 100 Pine Tree Dr, Willobrugh PA'
print(gma_addr)
gma_addr = gma_addr.replace('Grandma', 'Kathy DiFiglia')
print(gma_addr)

receipt_total = '$2,234.87'
receipt_total = receipt_total.replace('$', '').replace(',', '')
# receipt_total = receipt_total.replace(',', '')

print(float(receipt_total)) # converts the string to a float so we can do math with it

# Examples using input and string manipulation

checkin = input('Are you OK? (Enter Y or N): ').upper()
if checkin == 'Y':
    print('Oh good!')
else:
    print('Oh no!')

print(f'You entered: {checkin}')