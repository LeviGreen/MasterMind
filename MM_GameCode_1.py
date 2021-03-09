#LGreen - 3-8-2021: This is the program that simulates the game MasterMind that can be
#                   played through a terminal window.

#Rules: 
#1. Select four 1-digit numbers between 1-6, separated by one space. Then Press Enter. These numbers represent colors (1-Rd,2-Yl,3-Gn,4-Bu,5-Wh,6-Bk) (EX: '4 3 2 1')
#2. The Computer will output an array of numbers:
# a '1' means that you have selected a correct color in the sequence.
# a '2' means that you have selected a correct color and it's correct spot in the four color pattern.
#Note that you must use your own logic to determine which of your numbers that you chose correspond to which outputted number.
#3. Repeat step (1) modifying your selection based on all of your previous guesses and the computer's output.
#4 The game ends when either you have guessed all four colors and their correct spot in the four color pattern ([2, 2, 2, 2]) or you have exceeded 10 guesses.

import random
import time

def Initial():
    print("Let's play MasterMind!")
    time.sleep(1)
    print("Generating Pattern...")
    time.sleep(1)

def GeneratePattern():
    compArr = []
    i = 0
    while i < 4:
        compPick = random.randint(1,6)
        compArr.append(compPick)
        i = i + 1
    return compArr

def KnownPattern():
    return [1, 2, 1, 1]

def ComparePatterns(c0, c1, c2, c3, user):
    comp = [c0,c1,c2,c3]
    resultArr = []
    user = user.split()
    c = 0
    while c < 4:
        if int(user[c]) == comp[c]:
            resultArr.insert(0,2)
            user[c] = 0
            comp[c] = 0
        c = c + 1

    c = 0
    while c < 4:
        if int(user[c]) > 0 and int(user[c]) in comp:
            comp[comp.index(int(user[c]))] = 0
            resultArr.insert(0,1) 
        c = c + 1              

    print("          ",resultArr)
    return sum(resultArr)

clear = "\n" * 50
tries = 1
result = 0

Initial()
pattern = GeneratePattern()
#pattern = KnownPattern()
userPick = input("time to guess...Select 4 colors: ")
print
print(userPick)

while tries < 10 and result < 8:
    result = ComparePatterns(pattern[0],pattern[1],pattern[2],pattern[3], userPick)
    tries = tries + 1
    if result < 8:
        userPick = input()

if tries <= 10:
    print("YOU WIN!!")
    print(pattern, "   ", userPick)
    
else:
    print("You lose :(")
    print(pattern)
