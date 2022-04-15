from tkinter import *
import RPi.GPIO as GPIO
import threading
import time

self = Tk()

right = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(right, GPIO.IN)

class button:
    
    def __init__(self, relief1 = GROOVE , relief2 = GROOVE):
    
        self.relief1 = relief1
        self.relief2 = relief2

    def buttonSelection(self, buttonNumber):
        
        time.sleep(0.5)
        
        self.buttonNumber = buttonNumber
        
        if GPIO.input(right) == 1:
            self.buttonNumber += 1
        
        if self.buttonNumber == 1:
            self.relief1 = RAISED
            self.relief2 = GROOVE

        elif self.buttonNumber == 2:
            self.relief1 = GROOVE
            self.relief2 = RAISED
            
        elif self.buttonNumber > 2:
            self.buttonNumber = 1
            
        return self.relief1, self.relief2, self.buttonNumber

def updateSelection():
    
    buttonNumber = 0
    
    while True:   
        time.sleep(0.1)

        resx = self.winfo_screenwidth()
        resy = self.winfo_screenheight()

        self.title("Start Screen")
        self.geometry(str(resx)+"x"+str(resy))
        #self.geometry("320x240")
        self.attributes('-fullscreen', True)
        self.config(background = "black")
        #self.config(cursor="none")
        
        relief1, relief2, buttonNumber = button().buttonSelection(buttonNumber)
        Button1 = Button(self, text = "one", padx = 50, pady = 50, fg = "black", bg = "yellow", bd = 10, relief = relief1).place(relx = 0.25, rely = 0.5, anchor = CENTER)
        Button2 = Button(self, text = "two", padx = 50, pady = 50, fg = "black", bg = "yellow", bd = 10, relief = relief2).place(relx = 0.75, rely = 0.5, anchor = CENTER)
        
t2 = threading.Thread(target = updateSelection)
t2.start()
    
self.mainloop()
updateSelection()