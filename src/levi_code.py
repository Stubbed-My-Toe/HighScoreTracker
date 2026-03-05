import string, random, hashlib, json

#create function create account
def create_account():
    #get password and username with get info function
    pas,user,salt=get_info()
    pas,salt=pass_hash(pas,salt)
    with open('docs/accounts.json','r+') as fil:
        users=json.load(fil)
        #if username already exists
        if user in users:
            #tell user, and attempt to log in
            print('Account already exists.')
        #else
        else:
            #save password and username to file with empty spaces for highscores in the two games
            users[user]=[pas,salt,[[],[]],False]
            fil.truncate(0)
            fil.seek(0)
            json.dump(users,fil)
            print('Account created')


#create function get info
def get_info(set=True):
    #get user inputs for username and password
    user=input('What is the username? ')
    pas=input('What is the password? ')
    #loop while password is not strong (password strength function)
    if set:
        while not pass_strength(pas):
            #display password requirements and invalid password
            print('Weak password\nRequirements:\nMinimum 8 characters\nNeeds one of:\nUppercase letter\nLowercase letter\nNumber\nSpecial Character')
            #get new password from user
            pas=input('What is the new password? ')
    #call password hashing function on password
    salt=''.join(random.choices(string.ascii_lowercase+string.ascii_lowercase+string.digits+string.punctuation,k=8))
    #return hashed password and username
    return pas, user, salt

#create password hashing function, get PASS
def pass_hash(pas,salt):
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
def log_in():
    pas,user,salt=get_info(False)
    with open('docs/accounts.json','r') as fil:
        users=json.load(fil)
    #if PASS is the same as password saved with NAME
    try:
        if pass_hash(pas,users[user][1])[0]==users[user][0]:
            #return True
            return user
        #else
        else:
            #return False
            return False
    except:
        return False

#create function remove info, get username
def remove_info(user):
    with open('docs/accounts.json','r+') as fil:
        users=json.load(fil)
    #remove all information attached to (and) username
        del users[user]
        fil.truncate(0)
        fil.seek(0)
        json.dump(users,fil)

#create function change info, get old username
def change_info(user):
    #get password and username with get info function
    npas,nuser,salt=get_info()
    npas,salt=pass_hash(npas,salt)
    #assign highscores at old password and username to new password and username
    with open('docs/accounts.json','r+') as fil:
        users=json.load(fil)
        users[nuser]=[npas,salt,[[users[user][2][0]],[users[user][2][1]]],False]
        fil.truncate(0)
        fil.seek(0)
        json.dump(users,fil)
    #call function remove info on old username
    remove_info(user)

def check_admin(user):
    with open('docs/accounts.json','r') as fil:
        users=json.load(fil)
    if users[user][3]==True:
        return True
    else: return False

#create function admin
def admin():
    #loop
    while True:
        with open('docs/accounts.json','r') as fil:
            users=json.load(fil)
        #loop through and display usernames
        for i in range(len(users)):
            if i != 'admin':
                print(f'{i}. {list(users.keys())[i]}')
        #have user select a username
        slct=input('Select account, or anything else to exit: ')
        if slct not in [str(x) for x in range(len(users))]:
            break
        choice=input('1. Delete account\n2. Modify account login information\n')
        #if user wants to delete:
        if choice=='1':
            #call function remove info on username
            remove_info(list(users.keys())[int(slct)])
        elif choice=='2':
        #else if user wants to change login information
            #call function change info on username
            change_info(list(users.keys())[int(slct)])
