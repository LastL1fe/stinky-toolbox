#imports important modules
import json
from json.decoder import JSONDecodeError

import cv2 as cv
import serial

import calculate
import calibrate as c
import detection as dec
import sizematters as size

def resetPos():
    port.write("90:90,90:90\0".encode())

assBeLike = cv.VideoCapture(0)

if not assBeLike.isOpened():
    print("not openable dipshit")
    exit()

width = 600
height = 600
resize = size.rez(assBeLike, width, height)

port = serial.Serial("COM3", 9600)
resetPos()

try:
    jsonFile = open("calibration.json", "r")
except(Exception, JSONDecodeError):
    port.close()
    print("calibration information not found/corrupted: running calibration module")
    left = c.calibrate("Left").video(width, height)
    right = c.calibrate("Right").video(width, height)
    
settings = json.load(jsonFile)

leftServo = tuple(settings['Left Servos Calibration'].values())
rightServo = tuple(settings['Right Servos Calibration'].values())


xConst1, yConst1, xConst2, yConst2 = calculate.calc(width, height, leftServo, rightServo)

if __name__ == "__main__":
    dec.video(assBeLike, port, leftServo, rightServo, (xConst1, yConst1, xConst2, yConst2))






















#funni 69 numbr