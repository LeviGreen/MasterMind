#LGreen - 03/06/2021:   The purpose of this program is to prove that the RPi can act as an OhmMeter.
#                       If proven to be a viable option, each mastermind color will be assigned a color,
#                       and, when inserted into the board, the program will read the resistance value and
#                       determine which color the player has selected.


import RPi.GPIO as GPIO
import ADC0832
import time
from decimal import Decimal

Vc = 5.0

def init():
    ADC0832.setup()

def loop():
    
    Rk = input("Input Known R-value: ")
    print
    print "Vc = ",Vc
    print "Rk = ",Rk
    
    while True:
                Rt = input("Input Unknown [Theoretical] R-value: ")
                print "Rt = ",Rt
        
                digOut = ADC0832.getResult()            #Get reading from ADC
                Io = (Vc/Rk)*digOut / 255               #calculate amps output if 255 equals .5 A
                
                if Io > 0:        
                    Ra = ( Vc / Io ) - Rk       #calculate resistance, subtract the 10 Ohm known resistor
                    print 'Ra = ', Ra
                    
                else:                           #avoid div by 0 error
                    Ra = 1000
                    print "Ra = infinite"
        
                #print 'Io = ', Io
                print 'Do = ', digOut
                print '%  = ', (Ra/Rt)*100,'%'

if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt: 
        ADC0832.destroy()
        print ' U L8R !'
 