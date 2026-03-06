from accounts import *
from menu_profile import *

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
                game_menu(user)
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

main_menu()