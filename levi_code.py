import string, random, hashlib, json

#create function create account
def create_account():
    #get password and username with get info function
    user,pas=get_info()
    #if username already exists
        #tell user, and attempt to log in
    #else
        #save password and username to file with empty spaces for highscores in the two games

#create function get info
def get_info():
    #get user inputs for username and password
    user=input('What is the username? ')
    pas=input('What is the password? ')
    #loop while password is not strong (password strength function)
    while not pass_strength(pas):
        #display password requirements and invalid password
        print('Weak password\nRequirements:\nMinimum 8 characters\nNeeds one of:\nUppercase letter\nLowercase letter\nNumber\nSpecial Character')
        #get new password from user
        pas=input('What is the new password? ')
    #call password hashing function on password
    pas,salt=pass_hash(pas)
    #return hashed password and username
    return pas, user, salt

#create password hashing function, get PASS
def pass_hash(pas):
    salt=''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8))
    #hash PASS
    #return PASS and salt
    return hashlib.sha256((pas+salt).encode()).hexdigest(), salt

#create function password strength, get PASS
def pass_strength(pas):
    # set SCORE to 0
    score=0
    # if length of password is 8 or larger, add 1 to SCORE
    if len(pas)>=8: score+=1
    #create function check if, get LIST
    def check_if(listt):
        #   allow value modification
        nonlocal score
        # loop through characters in PASS
        for i in pas:
        #     if character in password is in LIST
            if i in listt:
        #         add one to score
                score+=1
        #         end loop
                break
    #call function check if on all uppercase letters
    check_if(string.ascii_uppercase)
    #call function check if on all lower letters
    check_if(string.ascii_lowercase)
    #call function check if on all numbers
    check_if(string.digits)
    #call function check if on all special characters
    check_if(string.punctuation)
    # if SCORE is 4, return true
    if score>=4: return True
    # else, return false
    else: return False

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