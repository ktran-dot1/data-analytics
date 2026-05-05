# Working with floor division

# Helpful patterns to get started:
# 1. start with the known
# 2. Calculate the unknown (what do you want to know)
# 3. Display Results

# How many cookies per student at the bake sale? How many cookies left over?

# Define the known
total_cookies = 34 + 28 + 56 + 22 + 12 + 78
students = 33

# Calculate the unknown

# cookies_per_student = total_cookies / students  # normal division

cookies_per_student = total_cookies // students # floor division
leftover_cookies = total_cookies % students  # remainder

# Display the results
print("Total cookies contributed: " + str(total_cookies))
print("Number of students: " + str(students))
print("Cookies per student: " + str(cookies_per_student))
print("Remaining cookies: " + str(leftover_cookies))


# Hours / minutes / seconds

length_of_recording = 1554  # seconds

# calculate in minutes:
minutes = length_of_recording // 60
seconds_left = length_of_recording % 60

# Display results
print()
print(minutes, "minutes", "and", seconds_left, "seconds")


