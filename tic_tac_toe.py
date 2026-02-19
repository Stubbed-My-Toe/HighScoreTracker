'''BEGIN Tic Tac Toe Game (2 Players)

   # SETUP
    - Create the board as 9 spaces numbered 1 through 9 like this:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
    
    - Player 1 uses "X", Player 2 uses "O"
    - Player 1 goes first
    - Ask both players for their names (to save winner scores later)
    - Keep track of how many moves have been made (stops at 9 for a tie)

    # GAMEPLAY
    - Show the current board after every move
    - Ask current player which number position they want to place their mark
    - Check if that position is empty (not already taken by X or O)
    - If it's taken, make them choose again
    - If it's empty, put their mark there and add 1 to move count

    # CHECKING FOR WINNER (after every move)
    - After each move, check if current player has 3 in a row:
        * Horizontal rows: positions (1,2,3) or (4,5,6) or (7,8,9)
        * Vertical columns: positions (1,4,7) or (2,5,8) or (3,6,9)
        * Diagonal lines: positions (1,5,9) or (3,5,7)
    
    - If they have 3 in a row, they win!
    - If all 9 moves are made and no winner, it's a tie

    # END OF GAME
    - If someone wins:
        * Show the final board
        * Announce the winner
        * Save the winner's name to "scores.txt" (Format: player_name,1)
          (The "1" means they won 1 game - can be used for leaderboard)
    
    - If tie:
        * Show final board
        * Announce it's a tie (no one gets a point)

    # SAMPLE OUTPUT
    Enter Player 1 name (X): Sam
    Enter Player 2 name (O): Jordan
    
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
    
    Player X choose position (1-9): 5
    
    1 | 2 | 3
    ---------
    4 | X | 6
    ---------
    7 | 8 | 9
    
    Player O choose position (1-9): 1
    
    O | 2 | 3
    ---------
    4 | X | 6
    ---------
    7 | 8 | 9
    
    (game continues until someone wins or tie)

END'''



