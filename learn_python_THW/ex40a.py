mystuff = {'apple' : "I AM APPLES! "}
print (mystuff['apple'])

import mystuff
mystuff.apple()
print (mystuff.tangerine)

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # get tangerine from module, but its a variable

class MyStuff(object): # creates a class called MyStuff
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self): #creates a function within this classs called apple()
        print (" I AM CLASSY APPLES!")

thing = MyStuff() # instantiates the class MyStuff, creates it in the form of variable thing
thing.apple()
print (thing.tangerine)

# dict style
mystuff['apples']

# module style
mystuff.apples()
print (mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print (thing.tangerine)
