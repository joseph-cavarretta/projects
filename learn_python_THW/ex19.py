# defines the function name as cheese_and_crackers, with 2 conditions. The function prints 4 lines below each time it is called.
def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print (f"you have {cheese_count} cheeses!")
    print (f"you have {boxes_of_crackers} crackers!")
    print ("Man that's enough for a party")
    print ("Get a blanket. \n")

#calls cheese_and_crackers with 2 numbers inputted as the values for the two variabe spots.
print ("We can just give the function numbers directly:")
cheese_and_crackers (20, 30)

#defines two variables and then uses them as the conditions of the function
print ("OR, we can use the variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers (amount_of_cheese, amount_of_crackers)

#calls the function with integer addition as the two condtions
print ("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

#calls th function with a variable + integer as each condition
print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
