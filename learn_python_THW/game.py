class Town(object):
    def enter(self):
        print("""
        You find yourself in an old western town. To your right is a Saloon.
        To your left is a bank. Do you head into the saloon or try to rob the bank?
        """
        choice = input("> ")

        if "saloon" in choice:
            enter(Saloon)
        else:
            enter(Jail)

class Saloon(object):
    def enter(self):
        print("""
        You kick open the swing doors of the saloon. The piano man rips
        to a halt. The sheriff immediately challenges you to a duel.
        Do you accept?
        """)
        choice = input("> ")
        if choice == yes:
            print("It's on. You both head out to the street.")
            enter(Duel)
        else:
            print("The sheriff shoots you on the spot. You dead.")
            death()

class Jail(object):
    def enter(self):
        print("""
        You majorly fail. The sheriff captures you.
        You are in jail until you die. You lose.
        """)
        death()

class Duel(object):
    def enter(self):
        print("""
        You stand back to back and begin you 10 paces.
        His finger feathers the trigger. He draws. You draw. Two shots fire.
        He falls to the ground dead. You win.
        """)
        exit(1)

def death():
    print ("Game over.")
    exit(1)

        
