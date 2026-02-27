# True's part of Highscore Tracker
#import Levi's code
from levi_code import *
#Import json
import json

#View Profile Function
def view_profile(user):
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
        with open("docs/accounts.json", "r") as fil:
            users = json.load(fil)
        print("Your Highscores:")
        print("Game 1:", users[user][2][0])
        print("Game 2:", users[user][2][0])
    #If User_Choice is set to 2
    elif user_choice == "2":
        change_info(user)
        print("Login Information Updated.")


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
            #Set user to login
            user = log_in()
            #If its successful print success
            if user:
                print("Login successful.")
            #Else
            else:
                print("Incorrect Login")
                #Print incorrect
        #If Choice is set to 2
        elif main_choice == "2":
            #Run Create Account
            create_account()
        #If Choice is set to 3
        elif main_choice == "3":
            #Print Exiting...
            print("Exiting...")
            #Break
            break

#Game_Menu Function
def game_menu(user):
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
                #Check if admin
            if check_admin(user):
                #If so run admin
                admin()
            #Else
            else:
                #print you are not an admin
                print("You are not an admin.")

        #If game_choice is set to 2
        elif game_choice == "2":
            #Run Game
            print("Game Starting...")
            #Call game
        #If game_choice is set to 3
        elif game_choice == "3":
            #Run View Profile
            view_profile(user)
        #If game_choice is set to 4
        elif game_choice == "4":
            #Print Exiting...
            print("Exiting...")
            #Break
            break

