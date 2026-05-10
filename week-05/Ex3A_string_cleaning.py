name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$72,000"

# use .lower() ro convert all three names to lowercase, and print each results
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# use .title()
print(name_1.title())
print(name_2.title())
print(name_3.title())

# remove the '$' using .replace()
new_salary1 = salary_1.replace("$", "")
print(new_salary1, type(new_salary1))
new_salary2 = salary_2.replace("$", "")
print(new_salary2, type(new_salary2))

# convert salary 1 into a usable integer
salary1 = int(salary_1.replace("$", "").replace(",", ""))
print(salary1, type(salary1))