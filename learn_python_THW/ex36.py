from sys import exit

def start():
    print ("You wake up in a dungeon. There are three doors in front of you. Which do you open?")

    choice = input(">> ")

    if "1" in choice:
        mancave()

    elif "2" in choice:
        ping_pong()

    elif "3" in choice:
        bathroom()

    else:
        print ("THAT. WAS. NOT. A. CHOICE.")
        start ()

def dead(why):
    print (why, "You are now dead. Nice work.")
    exit(0)

def mancave():
    print ("You find yourself in a man cave. There is a refrigerator, do you open it?")

    fridge = input (">> ")

    if fridge == "yes":
        print ("There are many beers. Do you drink them?")
        drunk = input(">> ")

        if drunk == "yes":
            print ("You are now drunk. Good job. You stumble out of the room and pass out.")
            print ("Hours later.....")
            start()

        else:
            print ("Oh no....")
            print ("There's something in here.")
            print ("Manbearpig hears you shut the door and awakens from his slumber.")
            dead ("He rips your arms and legs off and uses your body as decor.")
    else:
        dead ("Manbearpig appears and rips your head off.")

def ping_pong():
    print ("""You enter into a massive area.
There are hundreds of thousands of cheering fans in the stands,
shaking the ground with their roars.
In the center is a competition ping pong table.
You approach the table.
Across from you is Forrest Gump. You are handed a paddle.
It is a fight to the death.""")
    print ("\n")
    print ("will you serve the ball, or stab him in the neck with the paddle?")

    pong = input(">> ")

    if "serve" in pong:
        dead ("Forrest returns the serve at 170mph. The ball hits your face and instantly fractures your skull")

    elif "stab" in pong:
        print ("You win. You have defeated the shrimp king. You are rewarded with 100lbs of Bubba-Gump shrimp.")
        quit(0)

    else:
        print ("Choose again.")
        ping_pong()

def bathroom ():
    print ("""You are in a bathroom......or are you?
In front of you is a toilet and sink. The toilet smells of poo.
Do you flush?""")

    toilet = input(">> ")

    if toilet == "yes":
        print ("A gateway to the underworld opens at the bottom of the toilet bowl.")
        print ("Do you jump in?")

        jump = input (">> ")

        if "yes" in jump:
            dead ("""You jump in and land in hell.
You stand up and immediately get swamed by red horned demons who tie you up and force you do spend eternity
watching re-runs of Friends.""")

    elif toilet == "no":
        print ("The smell turns out to be a giant turd monster hiding behind the shower curtain")
        dead ("He smothers and absorbs you into his fecal body, and you become excrement.")

start()
