#LGreen - 3/11/2021: Now that I proved that the pi is able to dfferentiate color by assigning each color to a 
#                    Resistance Value, the purpose of this program is to integrate the MM_GameCode_1 program
#                    with the MM_OhmMeter_Test program by playing the game by manually switching the resistance
#                    inputs and submitting a color-pattern guess. To view schematic for how to set up the pi,
#                    see MM_ManualChange.pdf

#Rules: 
# 1. Install essential peripherals
#   a. Install termcolor in terminal
#   b. Make sure ADC0832 python files are downloaded
#   c. Wire Raspberry Pi according to diagram in MM_ManualChange.pdf
# 2. Run program from terminal : python MM_ManualChange.py
# 3. The Program will show you a short prompt and then the game will begin. 
# 4. The object of the game is to guess the computer's pattern of four colors in the correct order. 
#    For the first round, simply guess any four of the colors in any order (duplicates are allowed).
#    To select the first color in the first collumn, move the red wire on the Raspberry Pi to the corresponding
#    color and press enter. Once you press enter, the program will read your selection and prompt you to select
#    the 2nd columns' color. Do this for the 2nd, 3rd, and 4th columns' and press enter.
# 5. Once you have selected your fourth color and pressed enter, the program will output your selection along
#    with the result array. The result array will contain 2s and 1s. A "1" means that one of the selected colors
#    is correct, however, it is in the wrong color. A "2" means that one of the selected colors is both correct
#    and in the right column. (Note that you must deduce which colors the numbers in the result array are
#    referring to throughout the game).
# 6. Use the resulting result array to select the next row of four colors. For your convenience, the game as it
#    stands is reprinted after each round. 
# 7. To win, guess the computer's color pattern within 10 rounds.  
#   
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
    for x in range(4):
        compPick = random.randint(1,6) #Generate random int between 1 and 6.
        compArr.append(compPick)
    return compArr #Return pattern.

#Use for debugging. Designate the computer pattern.
def KnownPattern():
    return [2,2,2,2]

#Function to compare user input with computer pattern
def ComparePatterns(c0,c1,c2,c3,u0,u1,u2,u3):
    comp = [c0,c1,c2,c3] #Array to hold computer pattern
    user = [u0,u1,u2,u3]
    resultArr = [] #Declare empty array for outputted data.

    for c in range(4): #This for loop checks for right color and right spot.
        if int(user[c]) == comp[c]:  #if right color and spot...
            resultArr.insert(0,2)   #Add 2 to results array
            user[c] = 0             #clear user and comp array to 
            comp[c] = 0             #handle duplicate numbers. 

    for c in range(4): #This for loop checks for right color and wrong spot.
        if int(user[c]) > 0 and int(user[c]) in comp: #if user color is in comp pattern
            comp[comp.index(int(user[c]))] = 0 #clear comp array to handle duplicate numbers.
            resultArr.insert(0,1)       #Add 1 to results array.             

    runningScore.append(resultArr)
    return sum(resultArr)           #return sum of the resultsArr (8 = win)

#Prints the game as it stands to the terminal
def ShowRunningGame():
    for x in range(50):
        print
    i = 0
    for guess in runningGuess:
        print colored("0 ",colArr[guess[0]]),colored("0 ",colArr[guess[1]]),colored("0 ",colArr[guess[2]]),colored("0 ",colArr[guess[3]])
        print "          ",runningScore[i]
        i = i + 1 

#Method that runs at the end of game; either prints you won or lost depending if you won...or...lost.
def EndGame(result,pattern):
    ShowRunningGame()
    if result == 8:  
        print("YOU WIN!!")        
    else:
        print("You lose :(")
    print
    print colored('0 ',colArr[pattern[0]]),colored('0 ',colArr[pattern[1]]),colored('0 ',colArr[pattern[2]]),colored('0 ',colArr[pattern[3]])

#######################Code Start#########################################################################
    
tries = 0
result = 0

Initial()
pattern = GeneratePattern() #Generate Random Pattern
#pattern = KnownPattern()
print("time to guess four colors:")

while tries < 10 and result < 8: #gives user 10 tries to get right answer.
    userPick = MM_UserPickPattern.UserPickPattern() #prompt user to pick another pattern
    runningGuess.append(userPick) #update r.g. array
    result = ComparePatterns(pattern[0],pattern[1],pattern[2],pattern[3], userPick[0],userPick[1],userPick[2],userPick[3])
    ShowRunningGame()
    tries = tries + 1 #increment try count.

EndGame(result,pattern)


    