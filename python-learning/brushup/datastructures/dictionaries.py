# We’ll now do an exercise that you must study very carefully. I want you to type this code in and try to
# understand what’s going on. Take note of when you put things in a dict, get them from a hash, and
# all the operations you use. Notice how this example is mapping states to their abbreviations and then
# the abbreviations to cities in the states. Remember, mapping (or associating) is the key concept in a
# dictionary.

# Create a mapping of states and their abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# create a basic set of states and some cities in them
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print('-' * 10)

print("ny state has : ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every city in state
print('*' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

# Now let's do both at the same time
print('-' * 10)
print(states)
print(cities)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated as {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# Safely get an abbreviation by state taht might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas")

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for state 'TX' is {city}")