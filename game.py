import random ## Imports random module built-in with python
number = random.randint(1, 15) ## Sets the numbers to choose between


player_name = input("Hello, what's your name?") ## Allows input from the user, will pause execution until input has been made -- assigned to a variable without any keywords
number_of_guesses = 0 ## Number of guesses assigned to a variable (again without any keywords)
print('Okay! '+ player_name+ ', I am guessing a number between 1 and 15:') ## Print is like console.log for Python, also shows an example of string interpolation 

while number_of_guesses < 5: ## While loop saying that while number_of_guesses variable is less than 5, continue to execute the code block 
    guess = int(input())    ## Assigning the guess variable the value of the player's guess, converted from a string to an integer with int()
    number_of_guesses += 1  ## Incrementing the number of guesses counter
    if guess < number:
        print('Your guess is too low!')
    if guess > number:
        print('Your guess is too high!')
    if guess == number:
        break       ## End of while loop code block, will break if player guesses the correct number
## If guess reaches 5 or if guessed correctly, code underneath this line will then run
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries! Great! 😁')
else:
    print('You did not guess the number!😞 The number was ' + str(number) + '! Better luck next time!')