# TE 2nd Tic-Tac-Toe in Pseudocode.

# import random for a random number generator to select a box to put an O in.
import random
# Loop to loop the game if the user wants to keep going:
while True:
    # Board is also a list with the numbers
    board = [1,2,3,4,5,6,7,8,9]
    # Board is displayed as [1],[2],[3] one line down [4],[5],[6]one line down [7],[8],[9]
    print(f"{board[0]},{board[1]},{board[2]}\n{board[3]},{board[4]},{board[5]}\n{board[6]},{board[7]},{board[8]}")
    #Loop for player an computer turn:
    while True:
        # Computer variable is set to a random integer between 1 & 9
        computer = random.randint(1,9)
        # Player variable is set to an input where the player chooses a number on the gameboard
        player = int(input("Choose a number from the board to place your O: "))
        # If player selects a number in game board change it to O
        if player in board:
            board[player - 1] = 'O'
        # If computer selects number in game board change it to X
        if computer in board:
            board[computer - 1] = 'X'
        # Print the board after each turn
        print(f"{board[0]},{board[1]},{board[2]}\n{board[3]},{board[4]},{board[5]}\n{board[6]},{board[7]},{board[8]}")
        # Check for win conditions:
    # If player gets [1],[2],[3] then they win
    if board[0] == board[1] == board[2] == 'O':
        print("You win!")
        break
    # If player gets [4],[5],[6] then they win
    if board[3] == board[4] == board[5] == 'O':
        print("You win!")
        break
    # If player gets [7],[8],[9] then they win
    if 
    # If player gets [1],[5],[9] then they win
    # If player gets [7],[5],[3] then they win
    
    # If player gets [1],[4],[7] then they win
    # If player gets [2],[5],[8] then they win
    # If player gets [3],[6],[9] then they win

    # If computer gets [1],[2],[3] then thy win
    # If computer gets [4],[5],[6] then they win
    # If comuter gets [7],[8],[9] then they win
    
    # If computer gets [1],[5],[9] then they win
    # If computer gets [7],[5],[3] then they win
    
    # If computer gets [1],[4],[7] then they win
    # If computer gets [2],[5],[8] then they win
    # If computer gets [3],[6],[9] then they win
    # If this has looped 3 times then break while loop and ask player if they want to exit or keep going.




    