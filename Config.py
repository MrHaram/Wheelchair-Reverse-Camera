from tkinter import *
import threading

from LED import *
from Buzzer import *
from Joystick import *

led = led()
buzzer = buzzer()
button = button()

with open("Config.txt", "r") as configFile:
    savedColour = configFile.read()

def ledSwitch():
    ledStatus = led.getLedStatus()

    if ledStatus == False:
        led.setLedStatus(True)
        
    else:
        led.setLedStatus(False)

def buzzerSwitch():
    buzzerStatus = buzzer.getBuzzerStatus()
    
    if buzzerStatus == False:
        buzzer.setBuzzerStatus(True)
        
    else:
        buzzer.setBuzzerStatus(False)

class overlay:
    
    def __init__(self, overlayStatus):
        
        self.overlayStatus = overlayStatus

    def getOverlayStatus(self):
        return self.overlayStatus

    def setOverlayStatus(self):
        
        if self.overlayStatus == False:
            self.overlayStatus = True
            
        else:
            self.overlayStatus = False

class colour:  

    def __init__(self, colour):
        
        self.currentColour = colour

    def getColour(self):
        
        configFile = open("Config.txt", "r")
        currentColour = configFile.read()
        configFile.close()
        
        return currentColour
        
    def setColour1(self):
        
        self.configFile = open("Config.txt", "w")
        self.configFile.write("Yellow")
        self.configFile.close()
        
    def setColour2(self):
        
        self.configFile = open("Config.txt", "w")
        self.configFile.write("Light Blue")
        self.configFile.close()
        
    def setColour3(self):
        
        self.configFile = open("Config.txt", "w")
        self.configFile.write("Pink")
        self.configFile.close()

def back():
    button.buttonSelection(1, 1, 1)
    conf.destroy()

overlay = overlay(False)
colour = colour(savedColour)
currentColour = colour.getColour()

def configScreen():
    
    conf = Tk()
    
    conf.resx = conf.winfo_screenwidth()
    conf.resy = conf.winfo_screenheight()

    conf.title("Config Screen")
    conf.geometry(str(conf.resx)+"x"+str(conf.resy))
    conf.geometry("320x240")
    #conf.attributes('-fullscreen', True)
    conf.config(background = "Black")
    #conf.config(cursor="none")
        
    currentColour = colour.getColour()
    
    # buttonNumberX = 1
    # buttonNumberY = 1
    
    # relief1, relief2, relief3, relief4, relief5, relief6, relief7, buttonNumberX, buttonNumberY = button.buttonSelection(2, buttonNumberX, buttonNumberY)

    colour1 = Button(conf, command = colour.setColour1, text = "Yellow", font = "Arial", fg = "black", bg = "Yellow", bd = 10, relief = GROOVE).place(relx = 0.01, rely = 0.02, anchor = NW)
    colour2 = Button(conf, command = colour.setColour2, text = "Light Blue", font = "Arial", fg = "black", bg = "Light Blue", bd = 10, relief = GROOVE).place(relx = 0.5, rely = 0.02, anchor = N)
    colour3 = Button(conf, command = colour.setColour3, text = "Pink", font = "Arial", fg = "black", bg = "Pink", padx = 20, bd = 10, relief = GROOVE).place(relx = 0.99, rely = 0.02, anchor = NE)
    
    ledButton = Button(conf, command = ledSwitch, text = "LED", font = "Arial", fg = "black", bg = currentColour, padx = 50, bd = 10, relief = GROOVE).place(relx = 0.01, rely = 0.4, anchor = NW)
    buzzerButton = Button(conf, command = buzzerSwitch, text = "Buzzer", font = "Arial", fg = "black", bg = currentColour, padx = 41, bd = 10, relief = GROOVE).place(relx = 0.99, rely = 0.4, anchor = NE)
    overlayButton = Button(conf, command = overlay.setOverlayStatus, text = "Overlay", font = "Arial", fg = "Black", bg = currentColour, padx = 38, bd = 10, relief = GROOVE).place(relx = 0.01, rely = 0.77, anchor = NW)
    backButton = Button(conf, command = conf.destroy, text = "Back", font = "Arial", fg = "black", bg = currentColour, padx = 48, bd = 10, relief = GROOVE).place(relx = 0.99, rely = 0.77, anchor = NE)
    
    conf.mainloop()

#configMenu()
