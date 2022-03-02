
import time
# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward", "ok"]
actions = ["attack", "flee"]
rightActions =["rest", "carry on"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print(name.upper() +"! Let us go on a quest!")
time.sleep(1)
weapon = input("You can only bring one weapon. What weapon are you bringing?\n")
print("You enter the dark forest")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/ no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are a coward. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a bear.")
    time.sleep(1)
    print("To your right, there is more forest.")
    time.sleep(1)
    print("There is a rock wall directly in front of you.")
    time.sleep(1)
    print("Behind you is the forest exit.\n")
    time.sleep(1)
    response = input("What direction do you move?\nleft\nright\nforward\nbackward\n")
    if response == "left":
        print("The bear roars") #follow on from here
    elif response == "right":
        print("You head deeper into the forest.\n")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")


if response == "left":
    while response not in actions:
        print("Struck with fear, you are faced with a choice")
        response = input("Do you attack him? Or do you try to flee?\nattack\nflee\n")
        if response == "attack":
            print("You fearlessly draw your " + weapon + " and plunge it into the bear's stomach")
            time.sleep(1)
            print("The bear screams in anguish")
            time.sleep(1)
            print("'Oww WTF?' cries the bear")
            print("suddenly, two more bears come running in response")
            time.sleep(1)
            print("They surround you and begin to maul your face")
            time.sleep(1.5)
            print("You are in agony")
            time.sleep(1)
            print("You are dead")
            quit()

        elif response == "flee":
            print("You turn on your heels and sprint as fast as you can into the forest")
            time.sleep(0.5)
            print("The bear stamps the ground and begins to give chase")
            time.sleep(0.5)
            print("As you get into the depths of the forest, the bear loses interest and slowly gives up")
            time.sleep(1)
            print("While you begin to catch your breath you realise you are well into the forest")
            time.sleep(1)
            print("Fatigued and breathless, you press on.\n")
            quit()


#FOREST
if response == "right":
    while response not in rightActions:
            print("As the trees get thicker, the light grows dimmer")
            time.sleep(1)
            print("After walking for hours, the temperature begins to drop; the night is looming")
            time.sleep(1)
            print("You see a cave")
            response = input("Do you go inside to take a rest or carry on through the forest?\nrest\ncarry on\n")
            if response == "rest":
                print("Have a snooze.")
                quit()

            elif response == "carry on":
                print("You run into the bear's brother, who is conveniently better at hiding")
                time.sleep(1)
                print("He's also more forgiving than his brother, he lets you pass and you get back home")
                time.sleep(1)
                quit()
            