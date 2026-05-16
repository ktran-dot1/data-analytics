class Restaurant:
    '''Restaurant'''

    def __init__(self, rest_name, food_type):
        self.name = rest_name
        self.food = food_type

    def describe_rest(self): # Method 1
        return f"{self.name} serves {self.food}"
    
    def rest_open(self): # method 2
        return f"{self.name} is open."
    
# create three instances
rest1 = Restaurant('Weeby', 'Burgers')
rest2 = Restaurant('Donking Dunnts', 'Donuts')
rest3 = Restaurant('Bizza Hot', 'Pizza')


# Call each method for each instance
print(rest1.describe_rest())
print(rest1.rest_open())
print()
print(rest2.describe_rest())
print(rest2.rest_open())
print()
print(rest3.describe_rest())
print(rest3.rest_open())


