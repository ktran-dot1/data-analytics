import random

products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]

# # use random.choice()
prod_of_day = random.choice(products)
print(f"The product of the day is: {prod_of_day}")

# 3 products
survey_prod = random.sample(products, 3)
print(f"Survey products: {survey_prod}")

# Use random.shuffle() to shuffle the
# products list, then print the shuffled list.
random.shuffle(products)
print(f"The product list is: {products}")

# random transaction count
transaction = random.randint(50, 300)
print(f"Daily transaction count: {transaction}")
