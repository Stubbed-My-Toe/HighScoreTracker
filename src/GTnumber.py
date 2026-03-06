
def game():
    import random
    import json

    # SETUP
    print("Welcome to the Guess the Number Game!")


    # Computer picks a random number
    secret_number = random.randint(1, 100)

    # Create variable to count guesses
    guesses = 0

    # GAMEPLAY
    while True:
        # Get player's guess
        guess = int(input("Guess a number between 1 and 100: "))
        
        # Add 1 to guess count
        guesses = guesses + 1
        
        # Check if guess is correct
        if guess == secret_number:
            # END OF GAME
            print("Yor score was " + str(guesses))
            break
            
        # Give hints if wrong
        elif guess < secret_number:
            print("Too low, try again")
        
        else:
            print("Too high, try again")


    return guesses
