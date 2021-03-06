#LGreen - 3/11/2021: Now that I proved that the pi is able to dfferentiate color by assigning each color to a 
#                    Resistance Value, the purpose of this program is to integrate the MM_GameCode_1 program
#                    with the MM_OhmMeter_Test program by playing the game by manually switching the resistance
#                    inputs and submitting a color-pattern guess. To view schematic for how to set up the pi,
#                    see MM_ManualChange.pdf

#Rules: 
#TODO: Write out instructions on how to use.
#1. Make sure you have termcolor imported onto your system.
#   From Terminal: $ pip3 install termcolor


import RPi.GPIO as GPIO
import ADC0832
from decimal import Decimal
from termcolor import colored
import random
import time
import MM_UserPickPattern

colArr = ['cyan','red','yellow','green','blue','white','magenta']
runningGuess = []
runningScore = []

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
    return [2,2,2,2]
#Function to compare user input with computer pattern
def ComparePatterns(c0,c1,c2,c3,u0,u1,u2,u3):
    comp = [c0,c1,c2,c3] #Array to hold computer pattern
    user = [u0,u1,u2,u3]
    resultArr = [] #Declare empty array for outputted data.

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

    runningScore.append(resultArr)
    return sum(resultArr)           #return sum of the resultsArr (8 = win)


def ShowRunningGame():
    for x in range(50):
        print
    i = 0
    for guess in runningGuess:
        print colored("0 ",colArr[guess[0]]),colored("0 ",colArr[guess[1]]),colored("0 ",colArr[guess[2]]),colored("0 ",colArr[guess[3]])
        print "          ",runningScore[i]
        i = i + 1 

#######################Code Start#########################################################################
tries = 1
result = 0

Initial()
pattern = GeneratePattern() #Generate Random Pattern
#pattern = KnownPattern()

print("time to guess four colors:")

while tries <= 10 and result < 8: #gives user 10 tries to get right answer.
    userPick = MM_UserPickPattern.UserPickPattern()
    runningGuess.append(userPick)
    result = ComparePatterns(pattern[0],pattern[1],pattern[2],pattern[3], userPick[0],userPick[1],userPick[2],userPick[3])
    
    ShowRunningGame()
    
    tries = tries + 1 #increment try count.        

if result == 8:  
    ShowRunningGame()
    print("YOU WIN!!")
    print
    print colored('0 ',colArr[pattern[0]]),colored('0 ',colArr[pattern[1]]),colored('0 ',colArr[pattern[2]]),colored('0 ',colArr[pattern[3]])
    
else:
    ShowRunningGame()
    print("You lose :(")
    print
    print colored('0 ',colArr[pattern[0]]),colored('0 ',colArr[pattern[1]]),colored('0 ',colArr[pattern[2]]),colored('0 ',colArr[pattern[3]])