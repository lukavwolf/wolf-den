import random
import time

def menu():

    print()
    print("Welcome to my TEST game!")
    print()
    time.sleep(4)


menu()


def game1():
    print()
    print("You walk into the market to get groceries.")
    time.sleep(3)
    print("Upon reaching the register, a masked figure appears with a gun.")
    time.sleep(3)
    print('"Give me all your money," he says, "or the old lady gets it!"')
    time.sleep(3)
    print("He points the gun at the market owner.")
    time.sleep(3)
    print()
    ch1 = input("Do you give the robber your money? [Y/N]: ")
    print()

    if ch1 in ['Y', 'y']:
        print("Good choice! The robber takes your money and begins to count it out.")
        time.sleep(3)
        print()
        game2()

    else:
        print("The robber scoffs before shooting the old woman dead.")
        time.sleep(3)
        print()
        print("Game Over.")
        time.sleep(3)
        print()
        print("Try Again!")
        print()
        time.sleep(3)
        game1()


def game2():
    
    print()
    print("While the robber is counting out the funds, you see an opportunity to strike.")
    print()
    time.sleep(3)
    print("There are two viable options: an umbrella and a bag of chips.")
    print()
    time.sleep(3)
    ch2 = input("Which option do you go for? [Umbrella/Chips]: ")
    print()
    time.sleep(3)

    if ch2 in ['Umbrella', 'umbrella']:
        print()
        print("You grab for the umbrella, swinging with all your might.")
        time.sleep(3)
        print("The umbrella breaks against the man, falling to the ground in pieces.")
        time.sleep(3)
        print("The robber laughs before shooting you in the face.")
        print()
        time.sleep(4)
        print("Game Over.")
        time.sleep(3)
        print()
        print("Try Again!")
        print()
        time.sleep(3)
        game2()
    
    else:
        print()
        print("You grab the bag of chips, smashing it against the robber, crumbs and powder getting all over him.")
        time.sleep(3)
        print("He laughs, holding the gun at your face.")
        time.sleep(3)
        print("Suddenly, he starts sneezing uncontrollably.")
        time.sleep(3)
        print("It turns out, he's allergic to that particular brand of chips.")
        time.sleep(3)
        print("You take the chance, grabbing the gun and pointing it at him.")
        time.sleep(3)
        #game3()

#def game3():




game1()