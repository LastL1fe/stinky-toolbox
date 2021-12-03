#imports important modules
from json.decoder import JSONDecodeError
import json, serial, time
import calculate, detection as dec
import cv2 as cv, sizematters as size
import calibrate as c

def resetPos():
    port.write("90:90,90:90\0".encode())

assBeLike = cv.VideoCapture(0)
if not assBeLike.isOpened():
    print("not openable you dipshit")
    exit()

width = 600
height = 600
resize = size.rez(assBeLike, width, height)

port = serial.Serial("COM3", 9600)
resetPos()

try:
    jsonFile = open("calibration.json", "r")
except (Exception, JSONDecodeError):
    port.close()

    print("calibration information not found/corrupted: running calibration module")

    left = c.calibrate("Left").video(width, height)
    right = c.calibrate("Right").video(width, height)
    
    
settings = json.load(jsonFile)


leftServo = tuple(settings['Left Servos Calibration'].values())
rightServo = tuple(settings['Right Servos Calibration'].values())


xConst1, yConst1, xConst2, yConst2 = calculate.calc(width, height, leftServo, rightServo)

val = False

while 1:
    #Captures every frame of the video, processes it and then display it
    ret, cum = assBeLike.read()
    cum = cv.flip(cum, 1)
    grayScale = cv.cvtColor(cum, cv.COLOR_BGR2GRAY)

    time.sleep(0.015)
    dec.detectFace(cum, grayScale, port, val, (xConst1, yConst1), (xConst2, yConst2), leftServo, rightServo)
    cv.imshow("shiddy", cum)
    
    if cv.waitKey(20) == ord('q'):
        if not val:
            val = True
        else:
            val = False

    if cv.waitKey(10) == 27:
        break

time.sleep(1)

cv.destroyAllWindows()
resetPos()

port.close()

jsonFile.close()




#funni 69 numbr