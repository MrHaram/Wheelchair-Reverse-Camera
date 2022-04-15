import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

GPIO.setmode(GPIO.BOARD)

class led:
    
    def __init__(self, ledPin = 22, ledStatus = False):
    
        self.ledPin = ledPin
        self.ledStatus = ledStatus
        GPIO.setup(self.ledPin, GPIO.OUT)
    
    def getLedStatus(self):
        return self.ledStatus
    
    def setLedStatus(self, statusChange):
        self.ledStatus = statusChange
        
        if self.ledStatus == True:
            GPIO.output(self.ledPin, GPIO.HIGH)
            
        else:
            GPIO.output(self.ledPin, GPIO.LOW)