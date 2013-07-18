import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.output(4, False)
GPIO.output(17, False)
GPIO.output(27, False)
GPIO.output(22, False)
GPIO.output(18, False)
GPIO.output(23, False)
GPIO.output(24, False)
GPIO.output(25, False)

GPIO.cleanup()


print "Cleanup done"