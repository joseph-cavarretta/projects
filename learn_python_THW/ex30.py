people = 30
cars = 40
trucks = 15

# if more cars than people print this statement
if cars > people:
    print ("We should take the cars.")
# if above is not true, and cars are less than people, print this
elif cars < people:
    print ("We should not tak the cars.")
    # if neither of the above are true, print this
else:
    print ("We can't decide.")

# if there are more trucks than cars, print this
if trucks > cars:
    print ("That's too many trucks.")
# if the above is not true, and there are less trucls than cars, print this
elif trucks < cars:
    print ("Maybe we could take the trucks.")
# if neither of the above are true, print this
else:
    print ("We still can't decide.")
# if there are more people than trucks, print this
if people > trucks:
    print ("Alright, let's just take the trucks.")
# if th above is false, print this
else:
    print ("Fine, let's stay home then.")
