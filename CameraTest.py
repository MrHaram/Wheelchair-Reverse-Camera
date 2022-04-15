# Import required Libraries
import sys
from tkinter import *
from PIL import Image as imgs
from PIL import ImageTk, ImageDraw
import cv2
import threading
import numpy as np
import time

from Joystick import *
from UltrasonicSensor import *
from Buzzer import *
from LED import *
from Config import *

green = 16
red = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(green, GPIO.IN)
GPIO.setup(red, GPIO.IN)

#button = button()

def cam_setup():
    
    win = Tk()
    
    resx = win.winfo_screenwidth()
    resy = win.winfo_screenheight()
    
    win.title("Feed Screen")
    #win.geometry("320x240")
    win.geometry(str(resx)+"x"+str(resy))
    win.attributes('-fullscreen', True)
    win.config(background = "grey")
    #win.config(cursor="none")

    label = Label(win)
    label.place(relx = 0, rely = 0, anchor = NW)
    
    cap = cv2.VideoCapture(0)
    
    def updateSelection2():
    
        buttonNumberX = 1
        buttonNumberY = 0        
        
        def ultrasonicLabel():
            reading = (str("%.2f" % buzzer.buzzerInterval())+" cm")
            distanceReading = Label(win, text = reading, font = "Arial", fg = "black", bg = currentColour, padx = 10).place(relx = 0.5, rely = 0, anchor = N)

        while True:
            
            time.sleep(0.1)

            currentColour = colour.getColour()

            relief1, relief2, buttonNumberX, = button.buttonSelection(1, buttonNumberX, buttonNumberY)
            
            if buttonNumberX == 1 and GPIO.input(green) == 1:
                configScreen()
            
            elif (buttonNumberX == 2 and GPIO.input(green) == 1) or GPIO.input(red) == 1:
                win.destroy()
                sys.exit()
            
            optionsButton = Button(win, command = configScreen, text = "Options", font = "Arial", fg = "black", bg = currentColour, padx = 21, bd = 10, relief = relief1).grid(column = 0, row = 0)
            exitProgram = Button(win, command = sys.exit, text = "Exit", font = "Arial", fg = "black", bg = currentColour, padx = 20, bd = 10, relief = relief2).place(relx = 1, rely = 0, anchor = NE)

            ultrasonicLabel()
            
    t1 = threading.Thread(target = updateSelection2)  
    t1.start()
    
    cap.set(3, resy)
    cap.set(4, resx)
    
    # Define function to show frame   
    def show_frames():
        
        # Get the latest frame and convert into Image
        cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        img = imgs.fromarray(cv2image)
        flip = img.transpose(imgs.FLIP_TOP_BOTTOM)
        flip2 = flip.transpose(imgs.FLIP_LEFT_RIGHT)

        if overlay.getOverlayStatus() == True:
            
            draw = ImageDraw.Draw(flip2)
            
            # Right Line
            draw.line((resx * 0.17, resy * 0.83, resx * 0, resy * 0.89), fill = (255, 255, 0), width = 4)
            # Left Line
            draw.line((resx * 0.87, resy * 0.83, resx * 1, resy * 0.89), fill = (255, 255, 0), width = 4)
            
            # Green Line
            draw.line((resx * 0.17, resy * 0.83, resx * 0.87, resy * 0.83), fill = (0, 255, 0), width = 4)
            # Yellow Line
            draw.line((resx * 0.0, resy * 0.89, resx * 1, resy * 0.89), fill = (255, 255, 0), width = 4)
            # Red Line
            draw.line((resx * -0.5, resy * 0.97, resx * 1.1, resy * 0.97), fill = (255, 0, 0), width = 4)
            
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = flip2)
        label.imgtk = imgtk
        label.configure(image = imgtk)
        
        # Repeat after an interval to capture continiously
        label.after(20, show_frames)

    t2 = threading.Thread(target = show_frames)  
    t2.start()

    win.mainloop()
    #show_frames()
    
#cam_setup()
#win.mainloop()