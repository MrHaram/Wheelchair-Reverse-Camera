import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

from UltrasonicSensor import *

GPIO.setmode(GPIO.BOARD)

class buzzer:

    def __init__(self, _buzzerPin = 26, _buzzerStatus = False):

        self.buzzerPin = _buzzerPin
        self.buzzerStatus = _buzzerStatus
        GPIO.setup(self.buzzerPin, GPIO.OUT)

    def getBuzzerStatus(self):
        return self.buzzerStatus
    
    def setBuzzerStatus(self, statusChange):
        self.buzzerStatus = statusChange
        
        if self.buzzerStatus == True:
            GPIO.output(self.buzzerPin, GPIO.HIGH)
            
        else:
            GPIO.output(self.buzzerPin, GPIO.LOW)

    def buzzerInterval(self):
            
        #time.sleep(0.5)
        dis = distance()
        GPIO.output(self.buzzerPin, GPIO.LOW)
        
        #status = buzzer().getBuzzerStatus()
        
        if self.buzzerStatus == True and dis <= 25:
            for i in range(5):
                time.sleep(0.2)
                GPIO.output(self.buzzerPin, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(self.buzzerPin, GPIO.LOW)
                return dis
                
        elif self.buzzerStatus == True and dis <= 50:
            for i in range(5):
                time.sleep(0.3)
                GPIO.output(self.buzzerPin, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(self.buzzerPin, GPIO.LOW)
                return dis
                
        elif self.buzzerStatus == True and dis <= 100:
            for i in range(5):
                time.sleep(0.7)
                GPIO.output(self.buzzerPin, GPIO.HIGH)
                time.sleep(0.7)
                GPIO.output(self.buzzerPin, GPIO.LOW)
                return dis
                
        else:
            GPIO.output(self.buzzerPin, GPIO.LOW)
            return dis