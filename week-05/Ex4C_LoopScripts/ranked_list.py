foods = ["ramen", "tacos", "steak", "pasta", "rice"]

for index, food in enumerate(foods, start=1):
    if index == 1:
        print(f"{index}.{food} <-- Top Pick")
    else:
        print(f"{index}.{food}")


foods = ["ramen", "tacos", "steak", "pasta", "rice"]

for index, food in enumerate(reversed(food), start=1):
    print(f"{index}.{food}")