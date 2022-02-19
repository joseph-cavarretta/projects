#how many cars are avaialble#
cars = 100
#how many seats are in each car?#
space_in_a_car = 4.0
#how many drivers do we have today?#
drivers = 30
#How many passengers need a ride today?#
passengers = 90
#we only have so many drivers today, how many cars will actually be used?#
cars_not_driven = cars - drivers
#this is how many cars will actually be used#
cars_driven = drivers
#what is the total capacity of the cars we have to transport passengers?
carpool_capacity = cars_driven * space_in_a_car
#how many passengers should we put in each car?
average_passengers_per_car = passengers / cars_driven


print ("there are ", cars, " cars available")
print ("there are only ", drivers, " drivers available")
print ("there will be ", cars_not_driven, "empty cars today")
print ("we can transport ", carpool_capacity, " people today")
print ("we have ", passengers, " to carpool today")
print ("we need to put about ", average_passengers_per_car, " in each car")
