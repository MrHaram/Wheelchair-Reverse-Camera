import sys
from tkinter import *
import threading

from Config import *
from Joystick import *
from CameraTest import *

green = 16
red = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(green, GPIO.IN)
GPIO.setup(red, GPIO.IN)

self = Tk()

currentColour = colour.getColour()

def goFeedScreen():
    self.destroy()
    cam_setup()

def updateSelection1():
    
    buttonNumberX = 1
    buttonNumberY = 0 
    
    while True:   
        
        time.sleep(0.3)

        resx = self.winfo_screenwidth()
        resy = self.winfo_screenheight()

        self.title("Start Screen")
        self.geometry(str(resx)+"x"+str(resy))
        #self.geometry("320x240")
        self.attributes('-fullscreen', True)
        self.config(background = "black")
        #self.config(cursor="none")
        
        relief1, relief2, buttonNumberX = button.buttonSelection(1, buttonNumberX, buttonNumberY)
               
        if buttonNumberX == 1 and GPIO.input(green) == 1:
            goFeedScreen()
        
        elif (buttonNumberX == 2 and GPIO.input(green) == 1) or GPIO.input(red) == 1:
            self.destroy()
            sys.exit()
        
        startProgram = Button(self, text = "Start", font = "Arial", command = goFeedScreen, padx = 50, pady = 50, fg = "black", bg = currentColour, bd = 10, relief = relief1).place(relx = 0.25, rely = 0.5, anchor = CENTER)
        exitProgram = Button(self, text = "Exit", font = "Arial", command = sys.exit, padx = 50, pady = 50, fg = "black", bg = currentColour, bd = 10, relief = relief2).place(relx = 0.75, rely = 0.5, anchor = CENTER)
        
t1 = threading.Thread(target = updateSelection1)
t1.start()

self.mainloop()
updateSelection1()