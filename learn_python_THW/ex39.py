# create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI',
}

#create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville',
}

#add some more cities
cities['NY'] = 'New York'
cities ['OR'] = 'Portland'

#print out some cities
print ('-' * 10)
print ("NY state has: ", cities['NY'])
print ("OR state has: ", cities['OR'])

#print some states
print ("-" * 10)
print ("Michigan's abbrev is: ", states['Michigan'])
print ("Florida's abbrev is: ", states['Florida'])

#Do it by using the state then cities dict
print ("-" * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])

#print every state abbrev
print ("-" * 10)
for state, abbrev in list(states.items()):
    print (f"{state} is abbreviated {abbrev}.")

#print every city in state
print ('-' * 10)
for abbrev, city in list(cities.items()):
    print (f"{abbrev} has the city {city}.")

#now do both at the same time
print ("-" * 10)
for state, abbrev in list(states.items()):
    print (f"{state} state is abbreviated {abbrev}")
    print (f"and has city {cities[abbrev]}")

print ("-" * 10)
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print ("Sorry, no texas")

# get a city with a default value
city = cities.get('TX', 'does not exist')
print (f"The city for the state 'TX' is: {city}")

# do your own area
colorado = {
    'b' : 'boulder',
    'd' : 'denver',
    'e' : 'erie',
    'l' : 'longmont',
    's' : 'silverton'
}
print (colorado['b'])
print (colorado['d'])

for letter, town in list(colorado.items()):
    print (f"{letter} is for {town}")

print (colorado)

i = colorado.get('s')
print (i)
