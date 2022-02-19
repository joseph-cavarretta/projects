i = 0
numbers = []

while i < 6:
    numbers.append(i)
    i = i + 1
    print ("Numbers now: ", numbers)
    print (f"At the bottom, i is {i}.")

print ("the numbers: ")
for num in numbers:
    print (num)

def loop (list, increment):
    list = []
    i = 0
    while i < 6:
        list.append(i)
        i = i + increment
        print ("List now: ", list)

loop (list, 2)

def loop2 (list, increment):
    list = []
    for i in range (0, 6):
        list.append(i)
        i = i + increment
        print (list)

loop2 (list, 1)
