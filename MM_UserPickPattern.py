#LGreen - 3/11/2021: 

#Rules: 
#TODO: Write out instructions on how to use.
#1. Make sure you have termcolor imported onto your system.
#   From Terminal: $ pip3 install termcolor


import RPi.GPIO as GPIO
import ADC0832
from decimal import Decimal
import random
import time
from termcolor import colored

Vc = 5.0
Rk = 10.0

colArr = ['cyan','red','yellow','green','blue','white','magenta']

def UserPickPattern():
    uArr = []
    ADC0832.setup()
    
    for x in range(4):
                print"Move the red wire to your choice for the color in spot #",x+1," and press enter"
                raw_input()
                u = ADC0832.getResult()            #Get reading from ADC
                #print u
                if u > 248 and u < 252:
                    #uArr.append('red')
                    uArr.append(1)
                elif u > 231 and u < 235:
                    #uArr.append('yellow')
                    uArr.append(2)
                elif u > 126 and u < 130:
                    #uArr.append('green')
                    uArr.append(3)
                elif u > 244 and u < 246:
                    #uArr.append('blue')
                    uArr.append(4)
                elif u > 211 and u < 215:
                    #uArr.append('white')
                    uArr.append(5)
                elif u > 120 and u < 124:
                    #uArr.append('magenta')
                    uArr.append(6)
                else:
                    #uArr.append('cyan')
                    uArr.append(0)
                    
    print colored('0 ',colArr[uArr[0]]),colored('0 ',colArr[uArr[1]]),colored('0 ',colArr[uArr[2]]),colored('0 ',colArr[uArr[3]])
    return uArr            

if __name__ == '__main__':
    try:
        UserPickPattern()
    except KeyboardInterrupt: 
        ADC0832.destroy()
        print(' U L8R !')
    