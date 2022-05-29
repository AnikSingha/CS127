#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 13, 2021
#Rock Paper Scissors

import random

winner = ""
gameRunning = True

while gameRunning:
    userMove = int(input("enter 1 for rock, 2 for paper, or 3 for scissors:"))

    if userMove < 1:
        gameRunning = False

    pmove = random.randint(1,3)
    print("computerMove:", pmove)

    if userMove > 3:
        winner = "invalid"

    elif userMove - pmove == 0:   winner = "draw"

    elif userMove == 1:
        if pmove == 3:    winner = "human"
        else:   winner = "computer"

    elif userMove == 2:
        if pmove == 1:    winner = "human"
        else:   winner = "computer" 

    elif userMove == 3:
        if pmove == 2:    winner = "human"
        else:   winner = "computer"

    print("round finished and winner is:", winner)

