# original: http://dangerousprototypes.com/2012/10/04/driving-4-8x8-led-matrices-via-the-ht1632c-and-an-arduino/

#bibliotecas
import RPi.GPIO as GPIO
from time import sleep


delay = 0.008

def dataON():
    GPIO.output(DISPLAY_WR, False)
    sleep(delay)
    GPIO.output(DISPLAY_DATA, True)
    print 1
    sleep(delay)
    GPIO.output(DISPLAY_WR, True)
    sleep(delay)
    
def dataOFF():
    GPIO.output(DISPLAY_WR, False)
    sleep(delay)
    GPIO.output(DISPLAY_DATA, False)
    print 0
    sleep(delay)
    GPIO.output(DISPLAY_WR, True)
    sleep(delay)
    
def writeMatrix(array):
    GPIO.output(DISPLAY_CS, False)
    for index in range(len(array)):
        if array[index] == 1:
            dataON()
        else:
            dataOFF()
            
    GPIO.output(DISPLAY_CS, True)
    

# define pins
DISPLAY_CS      = 17
DISPLAY_WR      = 4
DISPLAY_DATA    = 22

# pins BCM nao BOARD
GPIO.setmode(GPIO.BCM)


# pins
GPIO.setup(DISPLAY_CS, GPIO.OUT)
GPIO.setup(DISPLAY_WR, GPIO.OUT)
GPIO.setup(DISPLAY_DATA, GPIO.OUT)

#tudo a zero
GPIO.output(DISPLAY_WR, False)
GPIO.output(DISPLAY_DATA, False)
GPIO.output(DISPLAY_CS, False)






# SYS EN 100 0000 0001 00 -----------------------------------------
GPIO.output(DISPLAY_CS, False)
sleep(delay)

dataON()
dataOFF()
dataOFF()

dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataON()

dataOFF()
dataOFF()
dataOFF()

GPIO.output(DISPLAY_CS, True)
sleep(delay)


# SYS EN 100 0000 0011 00 -----------------------------------------
GPIO.output(DISPLAY_CS, False)
sleep(delay)

dataON()
dataOFF()
dataOFF()

dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataON()
dataON()

dataOFF()
dataOFF()
dataOFF()

GPIO.output(DISPLAY_CS, True)
sleep(delay)

# WRITE 101 0000 0011 00 -----------------------------------------
"""
GPIO.output(DISPLAY_CS, False)
sleep(delay)

dataON()
dataOFF()
dataON()

dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataOFF()
dataOFF()

dataON()
dataON()
dataON()
dataON()




GPIO.output(DISPLAY_CS, True)
sleep(delay)
"""



led = [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1]
writeMatrix(led)

# reset pins
GPIO.cleanup()

# fim do programa
print "Fim"



# funcoes ------------------------------------------------

