# working with while loops
# keyboard shortcut to interrupt a while loop: ctrl + c 

# today_weather = input('What is today\'s weather? ')

# weather_report = []

# while today_weather != 'exit':
#     weather_report.append(today_weather)
#     print('Interesting, what is the next day\'s weather?')
#     today_weather = input('Next day weather (type \'exit\' to exit): ')

# print(f"Weather report: {weather_report}")

# counter = 0

# while counter < 10:
#     weather_report.append(today_weather)
#     counter += 1
#     print('Interesting, what is the next day\'s weather?')
#     today_weather = input('Next day weather: ')

# copying from p. 78 in the student guide

ice_cream_menu = [
    ('cone-single', 'chocolate', 4.00),
    ('cone-double', 'mint', 6.00),
    ('dish-single', 'cherry chip', 4.00)
]

order = input("What is your flavor order?")

for i in ice_cream_menu:
    for x in i:
        if order in str(x):
            print(i)