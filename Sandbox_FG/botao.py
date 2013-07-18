from time import sleep
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
 
while True:
        if ( GPIO.input(23) == False ):
                print "botao"
        
        sleep(0.1);