#Permite usar os pinos GPIO: 
import RPi.GPIO as GPIO
#permite usar sleep:
from time import sleep
 
LED_PIN = 17
 
print "Setting up GPIO"
# define que vamos usar a numeracao BCM dos pins GPIO, poderia ser BOARD:
# GPIO.setmode(GPIO.BOARD)    -> https://code.google.com/p/raspberry-gpio-python/wiki/BasicUsage
GPIO.setmode(GPIO.BCM)

# define LED_PIN (22) como output 
GPIO.setup(LED_PIN, GPIO.OUT)
 
 
 # declaracao da funcao enable_led
def enable_led(should_enable):
    if should_enable:
	GPIO.output(LED_PIN, True)
    else:
	GPIO.output(LED_PIN, False)
 
enable_led(False)
print "LED is OFF"
sleep(2)
enable_led(True)
print "LED is ON"
sleep(2)
enable_led(False)
print "LED is OFF"
sleep(2)
enable_led(True)
print "LED is ON"
sleep(2)

# faz reset a todos os pins GPIO
GPIO.cleanup()