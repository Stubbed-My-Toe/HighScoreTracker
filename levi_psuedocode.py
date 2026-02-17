

#create function create account
    #get password and username with get info function
    #if username already exists
        #tell user, and attempt to log in
    #else
        #save password and username to file with empty spaces for highscores in the two games

#create function get info
    #get user inputs for username and password
    #loop while password is not strong (password strength function)
        #display password requirements and invalid password
        #get new password from user
    #call password hashing function on password
    #return hashed password and username

#create password hashing function, get PASS
    #hash PASS
    #return PASS #yes i will make this better once i know how it works more

#create function password strength, get PASS
    # set SCORE to 0
    # if length of password is 8 or larger, add 1 to SCORE
    #create function check if, get LIST
        #   allow value modification
        # loop through characters in PASS
        #     if character in password is in LIST
        #         add one to score
        #         end loop
    #call function check if on all uppercase letters
    #call function check if on all lower letters
    #call function check if on all numbers
    #call function check if on all special characters
    # if SCORE is 4, return true
    # else, return false

#create function log in
    #get user information with function call get info
    #if PASS is the same as password saved with NAME
        #return True
    #else
        #return False

#create function remove info, get username
    #remove all information attached to (and) username

#create function change info, get old username
    #get password and username with get info function
    #assign highscores at old password and username to new password and username
    #call function remove info on old username

#create function admin
    #loop
        #loop through and display usernames
        #have user select a username
        #if user wants to delete:
            #call function remove info on username
        #else if user wants to change login information
            #call function change info on username