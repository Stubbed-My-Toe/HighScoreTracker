#IC CP2 1st period high score updater

#each thing will have a score, and the user will play games, and the indexes of 1-10 will be printed aned enumerated, excluding 0
#high scores is a dictionary ={
    #, correct_user:score 1, correct_user:score 2, correct_user:score 3, correct_user:score 4, correct_user:score 5, correct_user:score 6, correct_user:score 7, correct_user:score 8, correct_user:score 9, correct_user:score 10}.enumerate()
#when game high score comes in, check all of the user scores:
    #if score higher than score 10, then check 9, if higher, then 8, then 7, then 6, etc. until it reaches something it is not higher than, and then it will replace whatever was the last thing it was higher than