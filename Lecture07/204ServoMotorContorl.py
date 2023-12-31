# Servo motor control
#
#
#Program:204ServoMotorControl.py
#Date: 12/16/2023
#Author: X.Tang
#

import RPi.GPIO as GPIO
import time

OFFSE_DUTY = 0.5                  # define pulse offset if servo
SERVO_MIN_DUTY = 2.5 + OFFSE_DUTY # define the min angle of servo
SERVO_MAX_DUTY = 12.5 + OFFSE_DUTY # define the max angle of servo

servoPin = 12

def map(value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh - toLow)*(value - fromLow)/(fromHigh - fromLow) + toLow

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)   # using the physical GPIO numbering
    GPIO.setup(servoPin, GPIO.OUT)
    GPIO.setup(servoPin, GPIO.LOW)
    
    p = GPIO.PWM(servoPin, 50)  # set frequency to 50Hz
    p.start(0)                  # set initial duty cycle to 0
    
def servoWrite(angle):
    if(angle<0):
        angle = 0
    elif(angle>180):
        angle = 180
    p.ChangeDutyCycle(map(angle, 0, 180, SERVO_MIN_DUTY, SERVO_MAX_DUTY))
    
def loop():
    while True:
        for dc in range(0, 181, 1):  # make servo rotate from 0 to 180
            servoWrite(dc)
            time.sleep(0.001)
        time.sleep(1.5)
        
        for dc in range(180, -1, -1):  # make servo rotate from 180 to 0
            servoWrite(dc)
            time.sleep(0.001)
        time.sleep(1.5)
        
def destroy():
    p.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':  # program entrance
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # press ctrl + c to end the program
        destroy()
