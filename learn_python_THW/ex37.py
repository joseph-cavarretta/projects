x = 6
y = 6
if x and y == 6:
    print (True)

import sys as system

#assert x==5, "Error!"

while x < 7:
    print (x)
    x -= 1
    if x == 2:
        break

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
p1 = Person("Joe", 31)
print (p1.name)
print (p1.age)

while x < 8:
    print ("x is less than 8")
    x += 1
    continue
print ("it continued")

def new_x():
    x = 1
    print ("the new x is equal to 1")

dict = {"one":1, "two":2, "three":3, "four":4}
del dict["one"]
print (dict)

try:
    print ("hello")
except:
    print ("something went wrong")
else:
    print ("nothing went wrong")
finally:
    print ("ok done")

exec 'print ("hello")'

for i in range(1, 6):
    print (i)

global z

1 is 1 == True

a = lambda b, c, d: b + c + d

not True == False

True or False == True

def empty ():
    pass

h = -1
if h < 1:
    raise Exception("no numbers below zero please")

while True:
    pass

with h as a:
    print (a)

k = b"hello"

j = [1, 3, 5, 7]

print ("1\\2 and \' and \" and \a and \f and \n and \r and \t and \v")
