import RPi.GPIO as GPIO
import time

# Code used to manage the inputs from the joystick

# Used to setup pins
up = 7
down = 8
left = 10
right = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
GPIO.setup(left, GPIO.IN)
GPIO.setup(right, GPIO.IN)

while True:
    
        if GPIO.input(up) == 1:
            print("up")
        
        elif GPIO.input(down) == 1:
            print("down")
            
        elif GPIO.input(left) == 1:
            print("left")
            
            
        elif GPIO.input(right) == 1:
            print("down")
            
        else:
            print("-----")
            
        time.sleep(0.1)
            