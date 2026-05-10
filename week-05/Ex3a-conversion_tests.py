# Descriptions: This script tests various numeric
#               conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5'

# print variables and its type
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# cast as integer using int()
# print(int(a)) # ValueError
print(int(b))
# print(int(c)) # ValueError
# print(int(d)) # ValueError

# cast as float using float()
print(float(a))
print(float(b))
# print(float(c)) # ValueError
# print(float(d)) # ValueError

# for variable a, try to casting into a float then integer
print(int(float(a))) # outputs 101

# slicing to add just the numreric position of the string to a new variable
c_num = int(c[:3]) 
d_num = int(d[-2:]) # slicing from the end of the string

print(c_num, type(c_num))
print(d_num, type(d_num))

# for variable a and d, use the .strip() method to remove leading/trailing
# spaces, within a print statement to display each results
print(a.strip())
print(d.strip())