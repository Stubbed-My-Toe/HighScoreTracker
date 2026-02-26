# True's part of Highscore Tracker

#View Profile Function
    #Print What would you like to do
    #Print 1. View Your Highscores
    #Print 2. Change Login Information
    #User_Choice is set to an input asking to type 1 or 2.
    #If User_Choice is set to 1
        #Open User Profile File and show current and previous highscores.
    #If User_Choice is set to 2
        #username is set to an input asking user to type new username.
        #Save username in JSON file
        #password is set to an input asking user to type new password.
        #Save password in JSON file


#Main Function
    #While loop
        #1. Log in
        #2. Create account
        #3. Exit
        #Choice is set to a user input asking them to choose 1-3.
        #If Choice is set to 1
            #If Log In Returns True
                #Run Game_Menu
            #Else:
                #Print Incorrect Login.
        #If Choice is set to 2
            #Run Create Account
        #If Choice is set to 3
            #Print Exiting...
            #Break

#Game_Menu Function
    #While loop
        #1. Admin Log In
        #2. Play Games
        #3. View Profile
        #4. Exit
        #game_choice is seto to a user input asking them to choose 1-3.
        #If game_choice is set to 1
            #Run Admin Log In
        #If game_choice is set to 2
            #Run Game
        #If game_choice is set to 3
            #Run View Profile
        #If game_choice is set to 4
            #Print Exiting...
            #Break

