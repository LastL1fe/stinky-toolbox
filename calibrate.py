#calibrates servos maximum rotation to camera angle
import json
from json.decoder import JSONDecodeError
import cv2 as cv
import sizematters
import serial

#this took 4 months to make btw because i had to learn computer vision lmao

class calibrate:

    def __init__(self, name):
        
        self.data = {}
        self.name = name
        self.serPointX = 90
        self.xMax = 90
        self.xMin = 90
        self.serPointY = 90 
        self.yMax = 90
        self.yMin = 90
        try:
            self.port = serial.Serial('COM3', 9600, timeout = 0.02)
        except serial.SerialException:
            print("port not open, will continue with calibration")

    #reset the pos of the servos before running functions
    def resetPos(self):
        self.port.write("90:90,90:90\0".encode())

    def video(self, width, height):

        assBeLike = cv.VideoCapture(0)

        cv.namedWindow(self.name)
        cv.createTrackbar("X Slider: ", self.name, self.serPointX, 180, lambda val: self.Change(val, "X", self.xMin, self.xMax))
        cv.createTrackbar("Y Slider: ", self.name, self.serPointY, 180, lambda val: self.Change(val, "Y", self.yMin, self.yMax))
        cv.createButton("reset", self.resetButton, ("X Slider: ", "Y: Slider"))

        sizematters.rez(assBeLike, width, height)

        while 1:
            #Captures every frame of the video, processes it and then display it
            _, cum = assBeLike.read()
            cum = cv.flip(cum, 1)

            cv.imshow(self.name, cum)
       
            if cv.waitKey(10) == 27:
                self.updateJson()
                self.resetPos()
                self.port.close()
                cv.destroyAllWindows()
                break

    #checks if the value of the slider is within the acceptable range (between the min and max values)
    def Change(self, val, name, *args):

        if name == "X": self.serPointX = val #servo x value
        elif name == "Y": self.serPointY = val #servo y value

        accRange = range(args[0], args[1] + 1) #args[0] and args[1] are the min and max

        if val not in accRange:
            if val > args[1]: #sets max if val is higher than the instance's max
                if name == "X": self.xMax = val
                else: self.yMax = val
                print("{} max is: ".format(name) + str(args[1]))
            elif val < args[0]: #sets min if val is lower than the instance's max
                if name == "X": self.xMin = val
                else: self.yMin = val
                print("{} min is: ".format(name) + str(args[0]))
        else: #prints slider value
            print("{} value is: ".format(name) + str(val))

        #self explanatory haha cum
        if self.name == "Left":
            self.port.write("{}:{},90:90\0".format((self.serPointX), (self.serPointY)).encode())
        else:
            self.port.write("90:90,{}:{}\0".format((self.serPointX), (self.serPointY)).encode())

    def updateJson(self):  
        self.data = {
            "{}".format((self.name)) + " Servos Calibration":{
                "xPosRight": self.xMax,
                "xPosLeft": self.xMin,
                "yPosTop": self.yMin,
                "yPosBot": self.yMax
            }
        }  

        #kinda scuffed code, as of 1/15/22 i dont feel like changing it, fite me
        #overwrites existing calibration
        try:
            settings = json.load(open("calibration.json"))
            settings.update(self.data)

            with open("calibration.json", "w") as s:
                json.dump(settings, s)

        except (FileNotFoundError, JSONDecodeError):
            with open("calibration.json", "w") as settings:
                json.dump(self.data, settings)

    def resetButton(self, xTrackbar, yTrackBar):
        cv.setTrackbarPos(xTrackbar, self.name, 90)
        cv.setTrackbarPos(yTrackBar, self.name, 90)

#eat my ass 