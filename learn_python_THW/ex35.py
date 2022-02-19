from sys import exit

def gold_room ():
    print ("This room is full of gold. How much do you take?")
    choice = input("> ")
    how_much = int(choice)
    if how_much < 50:
        print ("Nice, you're not greedy. you win!")
        exit(0)

    elif how_much >= 50:
        dead ("You greedy bastard!")

    else:
        dead("Man, learn how to type a number.")

def bear_room ():
    print ("there is a bear in here.")
    print ("the bear has a bunch of honey.")
    print ("the fat bear is in front of another door.")
    print ("how are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("take honey, taunt bear, or open door? >> ")
        if choice == "take honey":
            dead("the bear looks at you and slaps your face off.")

        elif choice == "taunt bear" and not bear_moved:
            print ("the bear has moved from the door.")
            print ("you can go through it now.")
            bear_moved = True

        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets mad and east your legs off.")

        elif choice == "open door" and bear_moved:
            gold_room()

        else:
            print ("I got no idea what that means.")

def cthulhu_room ():
    print ("""Here you see the greatest evil Cthulhu.
He, it, whatever stares at you and you go insane.
Do you flee for your life or eat your head?""")

    choice = input ("> ")

    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("Well that was tasty.")

    else:
        cthulhu_room()

def dead (why):
    print (why, "Goodjob!")
    exit(0)

def start ():
    print ("""You are in a dark room.
There is a door to your right and left.
Which one do you take?""")

    choice = input ("> ")

    if choice == "left":
        bear_room()

    elif choice == "right":
        cthulhu_room()

    else:
        dead("You stumble around the room until you starve.")

start()
