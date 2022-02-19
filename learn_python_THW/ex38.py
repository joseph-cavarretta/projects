ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there are not 10 things in that list. Let's fix that")

stuff = ten_things.split(' ') #split(ten_things)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #pop(more_stuff) call 'pop' on more stuff / use 'pop' with arg more stuff
    print ("Adding: ", next_one)
    stuff.append(next_one) #append(next_one) call append on 'stuff' / use append with arg 'stuff'
    print (f"There are {len(stuff)} items now.")

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1])
print (stuff.pop()) #pop(stuff)
print (' '.join(stuff)) #join(stuff) call join on 'stuff' / use join with arg 'stuff'
print ("#".join(stuff[3:5])) #join(stuff[3:5])

Seltzer_types = ["la_croix", "kroger", "soleil", "bubly", "san_pelligrino", "dasani", "waterloo"]
dog_names = ["fido", "max", "morgan", "spike", "rover"]
sports = ["basketball", "baseball", "soccer", "football", "golf", "tennis"]
cities_CO = ["CO springs", "denver", "boulder", "ft collins", "pueblo", "ouray"]
