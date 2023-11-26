import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)


try:
    while True:
        GPIO.output(2, 1)  #turn on the LED
        time.sleep(1)      #wait for 1 sec
        GPIO.output(2, 0)  #turn off the LED
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
