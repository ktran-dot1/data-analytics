f = open("about_me.txt", 'r')
# print(f.read())
f.close()

# Print statement (50)
f = open("about_me.txt", 'r')
# print(f.read(50))
# print(f.read(50))
f.close()

# using readline
f = open("about_me.txt", 'r')
# f.readline(10)
# f.readline()
f.close()

# for i in range(1, 5):
    # print(f.readline())


f = open("about_me.txt", 'r')
# f.readline(1)
# f.readline(1)
# f.readline(10)
# f.readline(10)
# f.readline(100)
# f.readline(-1)
f.close()

f = open("about_me.txt", "r")
first_50 = f.read(50)
next_4_line = []
for i in range(4):
    next_4_line.append(f.readline())

next_100 = f.readline(100)
f.close()

print(f"First 50 characters: {first_50}")
print(f"The next four lines: {next_4_line}")
print(f"The next 100 charactors: {next_100}")


