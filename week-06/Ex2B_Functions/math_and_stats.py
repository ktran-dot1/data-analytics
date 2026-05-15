import random
import math
import statistics

vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3, 10)
pi = math.pi

# Experimenting with a subset of integers 1-100:
print("_Experimenting with a subset of integers 1-100:")
print(sum(vals_sample)) # Sum of 75 sample values from 1 to 100
print(statistics.mean(vals_sample)) # avg of 75 sample values
print(statistics.median(vals_sample)) # median of 75 sample values

# Experimenting with a superset of 200 values, integers 1-100
x = vals_choices
print("\n_Experimenting with a superset of 200 values, integers 1-100:")
print(statistics.mean(x)) # avg of 200 values
print(statistics.median(x)) # median of 200 values
print(statistics.mode(x)) # mode of 200 values
print(statistics.stdev(x)) # standard deviation of 200 values
print(statistics.variance(x))

# Modeling a random circle. Area = pi r**2
area = pi * (radius**2)
print("\n_Modeling a random circle:")
print(f"Radius = {radius}, area = {math.ceil(area)}") # rounded up to the nearest integer
print(f"Radius = {radius}, area = {math.floor(area)}") # rounded down to the nearest integer



