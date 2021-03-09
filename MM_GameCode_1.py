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
#Initial Start up instructions on screen.
def Initial():
    print("Let's play MasterMind! Read instructions at the top of the code to learn the rules.")
    time.sleep(1)
    print("Generating Pattern...")
    time.sleep(1)

#Function that generates a random pattern.
def GeneratePattern():
    compArr = [] #declare empty array
    i = 0
    while i < 4: 
        compPick = random.randint(1,6) #Generate random int between 1 and 6.
        compArr.append(compPick)
        i = i + 1
    return compArr #Return pattern.

#Use for debugging. Designate the computer pattern.
def KnownPattern():
    return [3,3,2,2]
#Function to compare user input with computer pattern
def ComparePatterns(c0, c1, c2, c3, user):
    comp = [c0,c1,c2,c3] #Array to hold computer pattern
    resultArr = [] #Declare empty array for outputted data.
    user = user.split() #take user string and split it into four integers.
    c = 0
    while c < 4: #This while loop checks for right color and right spot.
        if int(user[c]) == comp[c]:  #if right color and spot...
            resultArr.insert(0,2)   #Add 2 to results array
            user[c] = 0             #clear user and comp array to 
            comp[c] = 0             #handle duplicate numbers. 
        c = c + 1

    c = 0
    while c < 4: #This while loop checks for right color and wrong spot.
        if int(user[c]) > 0 and int(user[c]) in comp: #if user color is in comp pattern
            comp[comp.index(int(user[c]))] = 0 #clear comp array to handle duplicate numbers.
            resultArr.insert(0,1)       #Add 1 to results array.
        c = c + 1              

    print("          ",resultArr)
    return sum(resultArr)           #return sum of the resultsArr (8 = win)

tries = 1
result = 0

Initial()
pattern = GeneratePattern() #Generate Random Pattern
#pattern = KnownPattern()
userPick = input("time to guess...Select 4 colors: ")
print
print(userPick)

while tries < 10 and result < 8: #gives user 10 tries to get right answer.
    result = ComparePatterns(pattern[0],pattern[1],pattern[2],pattern[3], userPick)
    tries = tries + 1 #increment try count.
    if result < 8:  #Get new user input only if previous guess was wrong.
        userPick = input()

if result == 8:  
    print("YOU WIN!!")
    print(pattern, "   ", userPick)
    
else:
    print("You lose :(")
    print(pattern)
