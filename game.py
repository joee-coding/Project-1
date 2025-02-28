# we need the random "library"
from random import randrange

# makes a number between 0 and 100 (excluding 100)
# and saves it into a vriable called "ansnwer"
answer = randrange(100) 

# run the code inside of the while loop forever
while True:
    # ask the player for a number and save it
    player_guess = int(input("Guess a number:"))

    if (answer == player_guess):
        print("You win!")
        break # end the game by breaking the loop
    
    if (answer < player_guess):
        print("Smaller...")
    else:
        print("Bigger...")