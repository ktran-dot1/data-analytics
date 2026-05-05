# Examples of using assignment operators

# library example

joe = 0 # Joe has no books checked out when he gets his library member

# Joes checks out a book

joe += 1 # same as joe = joe + 1
joe = joe + 1
joe += 2

# Joe returns some books

joe -= 3

print("Books Joe has checked out of the library:", joe)

# Using F-string
print(f'Joe has {joe} book(s) checked out of the library')

joe += 1000

print(f'Oh geez, Joe has {joe:,} books checked out')

print(f'If Joe had checked out half as many books, he would have {joe / 2:.0f}')



