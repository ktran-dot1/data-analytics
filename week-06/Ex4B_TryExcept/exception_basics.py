# Exception Basics

#ValueError
try:
    x = int("Hello")

except ValueError:
    print("ValueError! Please try again.")

else:
    print(x)

finally:
    print("Let's try another one: \n")


# Name Error
try:
    k = banana
except NameError:
    print("NameError! That variable doesn't exist")

else:
    print(k)
finally:
    print("Let's try another one: \n")

# Type Error

try:
    y = "Hello world! + 5"
except TypeError:
    print("TypeError! can not add an int to a str")
else:
    print(y)
finally:
    print("Let's try another one: \n")

# Syntax Error
try:
    eval("1 + ")
except SyntaxError:
    print("SyntaxError! Incomplete expression")
else:
    print("Evaluation sucessful!")
finally:
    print("let's try another one: \n")

