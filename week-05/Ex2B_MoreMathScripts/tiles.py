# Tiling a room with dimensions L x W ft
# twelve tiles per box, each tile is 1 ft x 1 ft
# How many boxes of tiles do we need to buy? full boxes only, no partial boxes allowed
# Need at least 10% more tiles to account for breakage and cutting
import math

# How big is the room?
l = float(input("Enter the Length of the room in feet: "))
w = float(input("Enter the Width of the room in feet: "))

# What is the area of the room?
area = l * w

# How many tiles do we need to cover the area?
tiles_needed = area * 1.1 # 10% more tiles

# How many boxes of tiles do we need to buy?
boxes_needed = math.ceil(tiles_needed / 12) # 12 tiles per box

# Display the results
print(f"You need to buy {boxes_needed} boxes of tiles to cover the room.")
