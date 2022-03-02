from random import randint

#create a list of play options
choice = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = choice[randint(0,2)]

#set player to False
player = False

computerScore = 0
playerScore = 0

while player == False:
#set player to True
    player = input("\nWould you like to play Rock, Paper or Scissors? You can also check the Scores or Reset! ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("\nYou lose!", computer, "covers", player)
            computerScore += 1
            print("\nThe score is: You-"+ str(playerScore) + " Computer-" + str(computerScore))
        else:
            print("\nYou win!", player, "smashes", computer)
            playerScore += 1
            print("\nThe score is: You-"+ str(playerScore) + " Computer-" + str(computerScore))
    elif player == "Paper":
        if computer == "Scissors":
            print("\nYou lose!", computer, "cut", player)
            computerScore += 1
            print("\nThe score is: You-"+ str(playerScore) + " Computer-" + str(computerScore))
        else:
            print("\nYou win!", player, "covers", computer)
            playerScore += 1
            print("\nThe score is: You-"+ str(playerScore) + " Computer-" + str(computerScore))
    elif player == "Scissors":
        if computer == "Rock":
            print("\nYou lose...", computer, "smashes", player)
            computerScore += 1
            print("\nThe score is: You-"+ str(playerScore) + " Computer-" + str(computerScore))
        else:
            print("\nYou win!", player, "cut", computer)
            playerScore += 1
            print("\nThe score is: You-"+ str(playerScore) + " Computer-" + str(computerScore))
    if player == "Scores":
           print("\nThe score is: You-"+ str(playerScore) + " Computer-" + str(computerScore))
    elif player == "Reset":
        if playerScore < computerScore:
            print("\nWe won't tell anyone that you were being beat by the computer!🤭")
            playerScore = 0
            computerScore = 0
        if playerScore > computerScore:
            print("\n🤖:YOU ARE MERCIFUL TO US BOTS! YOU WILL BE SPARED...MAYBE")
            playerScore = 0
            computerScore = 0
        else:
            print("\n☯️Even though they were equal, the scores have been reset☯️")
            playerScore = 0
            computerScore = 0

    
   
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = choice[randint(0,2)]
    