# working with sets
print()
print('Creating a seating arrangement:')

attendees = {'Natalia', 'Sthefanie', 'Brandon', 'Dahlia'}

seat1, seat2, seat3, seat4 = attendees

print(f'Table 1 seats: {seat1}, {seat2}, {seat3}, {seat4}')

# Combine list with set of attendees
rsvp = ['Brandon', 'Dahlia', 'Destiney', 'Edmund']
attendees.update(rsvp) # use .update to combine list and sets
print(f'Updated for RSVPs: {attendees}')

attendees.add("Hritik") # use .add, when adding one more value
print(f'One more for the guest list: {attendees}')

# list: ordered, mutable(changeable), allows duplicates -- enclosed in []
# tuple: ordered, immutable, allows duplicated -- enclosed in ()
# set: unordered, semi-immutable, does not allow duplicates. -- enclosed in {}
# dictionary: ordered, changeable, does not allow duplicates


# working with dictionaries
print()
print("Dahlia's car")

dahlia_car = {
    "make": "Nissan",
    "model": "Rogue",
    "year": 2022,
    "color": "gray"                       
}

print(f'Dahlia owns a {dahlia_car['year']} {dahlia_car['make']} {dahlia_car['model']}')

parking_spaces = {1: 'Greg', 2: 'Sal', 3: 'Casey'}

print(f'Parking space 1 is assigned to {parking_spaces[1]}')

print(parking_spaces.items())
print(parking_spaces.keys())
print(parking_spaces.values())

print(f'Parking space 4 is assigned to {parking_spaces.get(4, '[no space available]')}')

parking_spaces[4] = 'Herman'
print(f'Parking space 4 is assigned to {parking_spaces.get(4, '[no space available]')}')

print(4 in parking_spaces)
print('Herman' in parking_spaces)
print(parking_spaces)  

# nested collections
print()

print("Working with nested collections")

# When might this be useful?
# biology: body > organs > cell
# geography: state > county > city > municipal district > neighborhoos
# taxonomy: kingdom > phylum > class > order > family > genus > species

employee = (
    ("emp_id", "name", "hire date", "salary"),
    ('007', "James Bond", "Nov 30, 2005", 128000),
    ('008', "Miss Moneypenny", "Apr 4, 2008", 148000),
    ('100', "Quigley Henry", "May 5, 2015", 178000)
)

print(f'This year the employee picnic is being run by {employee[1][1][0:5]}') # slicing to get the first name only

