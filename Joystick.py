from tkinter import *
import RPi.GPIO as GPIO
import threading
import time

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

class button:
    
    def __init__(self, relief1 = GROOVE , relief2 = GROOVE, relief3 = GROOVE, relief4 = GROOVE, relief5 = GROOVE, relief6 = GROOVE, relief7 = GROOVE):
    
        self.relief1 = relief1
        self.relief2 = relief2
        self.relief3 = relief3
        self.relief4 = relief4
        self.relief5 = relief5
        self.relief6 = relief6
        self.relief6 = relief6 


    def buttonSelection(self, pageNumber, buttonNumberX, buttonNumberY):
        
        time.sleep(0.3)
        
        self.pageNumber = pageNumber
        self.buttonNumberX = buttonNumberX
        self.buttonNumberY = buttonNumberY
        
        if pageNumber == 1:
        
            if GPIO.input(right) == 1:
                self.buttonNumberX += 1

            elif GPIO.input(left) == 1:
                self.buttonNumberX -= 1
                
            if self.buttonNumberX == 1:
                self.relief1 = RAISED
                self.relief2 = GROOVE

            elif self.buttonNumberX == 2:
                self.relief1 = GROOVE
                self.relief2 = RAISED
                
            elif self.buttonNumberX > 2:
                self.buttonNumberX = 1
                
            elif self.buttonNumberX == 0:
                self.buttonNumberX = 2
            
            return self.relief1, self.relief2, self.buttonNumberX

        elif pageNumber == 2:
            
            if GPIO.input(right) == 1 and self.buttonNumberY == 1:
                self.buttonNumberX += 1

            elif GPIO.input(left) == 1 and self.buttonNumberY == 1:
                self.buttonNumberX -= 1
                
            elif GPIO.input(up) == 1 and self.buttonNumberX == 1:
                self.buttonNumberY -= 1
                
            elif GPIO.input(down) == 1 and self.buttonNumberX == 1:
                self.buttonNumberY += 1
                
            if self.buttonNumberX == 1 and self.buttonNumberY == 1:
                self.relief1 = RAISED
                self.relief2 = GROOVE
                self.relief3 = GROOVE
                self.relief4 = GROOVE
                self.relief5 = GROOVE
                self.relief6 = GROOVE
                self.relief7 = GROOVE

            elif self.buttonNumberX == 2 and self.buttonNumberY == 1:
                self.relief1 = GROOVE
                self.relief2 = RAISED
                self.relief3 = GROOVE
                self.relief4 = GROOVE
                self.relief5 = GROOVE
                self.relief6 = GROOVE
                self.relief7 = GROOVE
                
            elif self.buttonNumberX == 3 and self.buttonNumberY == 1:
                self.relief1 = GROOVE
                self.relief2 = GROOVE
                self.relief3 = RAISED
                self.relief4 = GROOVE
                self.relief5 = GROOVE
                self.relief6 = GROOVE
                self.relief7 = GROOVE

            elif self.buttonNumberX == 1 and self.buttonNumberY == 2:
                self.relief1 = GROOVE
                self.relief2 = GROOVE
                self.relief3 = GROOVE
                self.relief4 = RAISED
                self.relief5 = GROOVE
                self.relief6 = GROOVE
                self.relief7 = GROOVE

            elif self.buttonNumberX == 2 and self.buttonNumberY == 2:
                self.relief1 = GROOVE
                self.relief2 = GROOVE
                self.relief3 = GROOVE
                self.relief4 = GROOVE
                self.relief5 = RAISED
                self.relief6 = GROOVE
                self.relief7 = GROOVE
                
            elif self.buttonNumberX == 1 and self.buttonNumberY == 3:
                self.relief1 = GROOVE
                self.relief2 = GROOVE
                self.relief3 = GROOVE
                self.relief4 = GROOVE
                self.relief5 = GROOVE
                self.relief6 = RAISED
                self.relief7 = GROOVE

            elif self.buttonNumberX == 2 and self.buttonNumberY == 3:
                self.relief1 = GROOVE
                self.relief2 = GROOVE
                self.relief3 = GROOVE
                self.relief4 = GROOVE
                self.relief5 = GROOVE
                self.relief6 = GROOVE
                self.relief7 = RAISED

            if self.buttonNumberY == 1:
            
                if self.buttonNumberX > 3:
                    self.buttonNumberX = 1
                    
                elif self.buttonNumberX < 1:
                    self.buttonNumberX = 3

            elif self.buttonNumberX > 1:

                if self.buttonNumberX > 2:
                    self.buttonNumberX = 1
                    
                elif self.buttonNumberX < 1:
                    self.buttonNumberX = 2

            elif self.buttonNumberY > 3:
                self.buttonNumberY = 1
                
            elif self.buttonNumberY < 1:
                    self.buttonNumberY = 3
                    
            return self.relief1, self.relief2, self.relief3, self.relief4, self.relief5, self.relief6, self.relief7, self.buttonNumberX, self.buttonNumberY