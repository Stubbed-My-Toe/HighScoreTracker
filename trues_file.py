# True's part of Highscore Tracker

#View Profile Function
def view_profile():
    #Print What would you like to do
    print("What would you like to do?")
    #Print 1. View Your Highscores
    print("1. View Your Highscores")
    #Print 2. Change Login Information
    print("2. Change Login Information")
    #User_Choice is set to an input asking to type 1 or 2.
    user_choice = input("Choose between 1 or 2: ")
    #If User_Choice is set to 1
    if user_choice == "1":
        #Open User Profile File and show current and previous highscores.
    #If User_Choice is set to 2
    elif user_choice == "2":
        #username is set to an input asking user to type new username.
        username = input("Type your new username: ")
        #Save username in JSON file
        #password is set to an input asking user to type new password.
        password = input("Type your new password")
        #Save password in JSON file


#Main Function
def main_menu():
    #While loop
    while True:
        #1. Log in
        print("1. Log in")
        #2. Create account
        print("2. Create account")
        #3. Exit
        print("3. Exit")
        #Choice is set to a user input asking them to choose 1-3.
        main_choice = input("Choose 1-3: ")
        #If Choice is set to 1
        if main_choice == "1":
            #If Log In Returns True
                #Run Game_Menu
            #Else:
                #Print Incorrect Login.
        #If Choice is set to 2
        elif main_choice == "2":
            #Run Create Account
        #If Choice is set to 3
            #Print Exiting...
            #Break

#Game_Menu Function
def game_menu():
    #While loop
    while True:
        #1. Admin Log In
        print("1. Admin Log In")
        #2. Play Games
        print("2. Play Games")
        #3. View Profile
        print("3. View Profile")
        #4. Exit
        print("4. Exit")
        #game_choice is seto to a user input asking them to choose 1-3.
        game_choice = input("Choose 1-3: ")
        #If game_choice is set to 1
        if game_choice == "1":
            #Run Admin Log In
        #If game_choice is set to 2
        elif game_choice == "2":
            #Run Game
        #If game_choice is set to 3
        elif game_choice == "3":
            #Run View Profile
            view_profile()
        #If game_choice is set to 4
        elif game_choice == "4":
            #Print Exiting...
            print("Exiting...")
            #Break
            break

