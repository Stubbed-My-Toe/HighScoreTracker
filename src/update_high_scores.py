#IC CP2 1st period high score updater

#each thing will have a score, and the user will play games, and the indexes of 1-10 will be printed aned enumerated, excluding 0
#high scores is a dictionary ={
    #, correct_user:score 1, correct_user:score 2, correct_user:score 3, correct_user:score 4, correct_user:score 5, correct_user:score 6, correct_user:score 7, correct_user:score 8, correct_user:score 9, correct_user:score 10}.enumerate(index 1 starting at 1 and index 10 ending at 10)
#when game high score comes in, check all of the user scores:
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

#then push all high scores to high scores csv