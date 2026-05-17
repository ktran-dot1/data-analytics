class Restaurant:
    '''Restaurant'''

    def __init__(self, rest_name, food_type):
        self.name = rest_name
        self.food = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self): # Method 1
        return f"{self.name} serves {self.food}"
    
    def rest_open(self): # method 2
        return f"{self.name} is open."
    
    def add_num_served(self):
        num_served = int(input("How many customers served today? "))
        self.number_served = num_served

    def print_num_served(self):
        print(f"{self.name} has served {self.number_served} customers")

    def customer_rating(self):
        rating = input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? ")
        
        # want an int for calculation
        if rating.isdigit():
            rating = int(rating) # cast as int

            if rating >= 1 or rating <= 5:
                self.customer_ratings.append(rating)

                # Find average rating
                average_rate = sum(self.customer_ratings) / len(self.customer_ratings)

                print(f"Your rating was {rating}")
                print(f"The average rating for this restaurant is {average_rate:.2f}")

            else:
                print("Please enter a valid number (1-5).")

        else:
            print("Please enter a whole number from 1-5.")


            


    
# create three instances
rest1 = Restaurant('Weeby', 'Burgers')
rest2 = Restaurant('Donking Dunnts', 'Donuts')
rest3 = Restaurant('Bizza Hot', 'Pizza')


# Call each method for each instance
print(rest1.print_num_served())
print(rest1.add_num_served())
print(rest1.print_num_served())

print(rest2.print_num_served())
print(rest2.add_num_served())
print(rest2.print_num_served())

print(rest3.print_num_served())
print(rest3.add_num_served())
print(rest3.print_num_served())

print(rest1.customer_rating())

