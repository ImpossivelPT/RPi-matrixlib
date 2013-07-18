# original: http://dangerousprototypes.com/2012/10/04/driving-4-8x8-led-matrices-via-the-ht1632c-and-an-arduino/

#bibliotecas
import RPi.GPIO as GPIO
from time import sleep

def dataON():
    GPIO.output(DISPLAY_WR, False)
    sleep(1)
    GPIO.output(DISPLAY_DATA, True)
    sleep(1)
    GPIO.output(DISPLAY_WR, True)
    sleep(1)
    
def dataOFF():
    GPIO.output(DISPLAY_WR, False)
    sleep(1)
    GPIO.output(DISPLAY_DATA, False)
    sleep(1)
    GPIO.output(DISPLAY_WR, True)
    sleep(1)

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




# SYS EN 100 0000 0001 00 -----------------------------------------
GPIO.output(DISPLAY_CS, False)
sleep(1)

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
sleep(1)

# SYS EN 100 0000 0011 00 -----------------------------------------
GPIO.output(DISPLAY_CS, False)
sleep(1)

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
sleep(1)

# SYS EN 101 0000 0011 00 -----------------------------------------
GPIO.output(DISPLAY_CS, False)
sleep(1)

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

dataOFF()
dataON()
dataON()
dataOFF()


GPIO.output(DISPLAY_CS, True)
sleep(1)

# reset pins
GPIO.cleanup()

# fim do programa
print "Fim"



# funcoes ------------------------------------------------

