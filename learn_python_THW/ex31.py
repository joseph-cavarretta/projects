print ("""You enter a dark room with 3 doors.
Do you go through door #1 , #2, or #3?""")

door = input ("> ")

if door == "1":
    print ("There's a giant bear here eating a cheese cake.")
    print ("What do you do?")
    print ("1. Take the cake.")
    print ("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print ("The bear eats your face off. Good job!")
    elif bear == "2":
        print ("The bear eats your legs off. Good job!")
    else:
        print (f"Well, doing {bear} is probably better.")
        print ("Bear runs away.")

elif door == "2":
    print ("You stare into the endless abyss at Cthulhu's retina.")
    print ("1. Blueberries.")
    print ("2. Yellow jacket clothespins.")
    print ("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print ("Your body survives powered y a mind of jello.")
        print ("Good job!")
    else:
        print ("The insanity rots your eye into a pool of muck.")
        print ("Good job!.")
elif door == "3":
    print ("What's good baby boi?")
    print ("Shawtay?")
    print ("Pimpin?")
    print ("Gucci?")

    whats_good = input("> ")

    if whats_good == "Shawtay":
        print ("Oh shyyyyyt")
    elif whats_good == "Pimpin":
        print ("Aye")
    elif whats_good == "Gucci":
        print ("Prada")
    else:
        print ("non-kewl")
else:
    print ("You stumble and fall on a knife and die. Good job!")
