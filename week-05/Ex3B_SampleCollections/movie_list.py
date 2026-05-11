movies = ["Scary Movie", "Grown Ups", "Trumen Show", "Madea"]
print(f"The list movies include my top {len(movies)} favorite movies")
print(movies)

# Using sort
print(sorted(movies))

# original list
print(movies)

# using .sort()
movies.sort()

# after .sort()
print(movies)

# the difference is that sorted() is only temporarily sorting the list
# while .sort() is permanent

# add another movie
movies.append("The Notebook")

print(f"The list movies includes my top {len(movies)} favorite movies")

print(movies)