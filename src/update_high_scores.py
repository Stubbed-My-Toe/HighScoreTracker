#IC CP2 1st period high score updater

import csv

def get_scores(path):
#each thing will have a score, and the user will play games, and the indexes of 1-10 will be printed and enumerated, excluding 0
#high scores is a dictionary ={
    with open(path,'r') as file:
        high_scores={}
        reader=csv.reader(file)
        for row in reader:
            high_scores.update({row.split(', ')[0]:row.split(', ')[1]})
    return high_scores
    #, correct_user:score 1, correct_user:score 2, correct_user:score 3, correct_user:score 4, correct_user:score 5, correct_user:score 6, correct_user:score 7, correct_user:score 8, correct_user:score 9, correct_user:score 10}.enumerate(index 1 starting at 1 and index 10 ending at 10)

def show_scores():
    print('\nGuess the number high scores:')
    for i, v in get_scores('docs/gtn_scores.csv').items().enumerate():
        print(f'{i}: {v[0]} got {v[1]}')
    print('\nTic tac toe high scores:')
    for i, v in get_scores('docs/gtn_scores.csv').items().enumerate():
        print(f'{i}: {v[0]} got {v[1]}')

def add_score(user,score,path):
    high_scores=get_scores(path)
    if len(high_scores)<10:
        x=len(high_scores)-1
    else:
        x=10
    #when game high score comes in, check all of the user scores:
    for i in range(x,-1,-1):
        if score > high_scores.values[x]:
            high_scores=dict(high_scores.items().insert(i,(user, score)))
            with open(path, 'w', newline='') as file:
                writer = csv.writer(file)
                for i in range(10):
                    writer.writerow([high_scores.keys[i],high_scores.values()[i]])
    #if score higher than score 10, then check 9, if higher, then 8, then 7, then 6, etc. until it reaches something it is not higher than, and then it will append ahead of whatever was the last thing it was higher than, using the key

#Read high scores,
#When high scores from games are imported, check highscores dictionary
#if high score > 10,
    #append ahead of 10
#elif highscore > 9 
    #append ahead of 9
#etc
#if highscore > than 1 
    #add to front of dictionary

#then push all high scores to high scores csv and save it