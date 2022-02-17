import requests
import cv2 as cv
import numpy as np
import threading
import json
import time
import sizematters

def createThread(img):
    swampyPus = threading.Thread(target=threadedShit, args=(img,))
    swampyPus.start()

def threadedShit(img):
    params = {
        "api_key": "UN5V5OR6z1c0cqj4k_-HZI8q1DBoEwq0",
        "api_secret": "-jVnsCfNvC-FG_3iGU1WHUMv5O6fIose",
        "image_file": img
    }

    data = requests.request(method="POST", url="https://api-us.faceplusplus.com/facepp/v3/detect", params=params)

    print(data.text)

camera = cv.VideoCapture(0)
sizematters.rez(camera, 600, 600)

time.sleep(1)

faceCascade = cv.CascadeClassifier("cascades/haarcascade_frontalface_alt2.xml")

facialRecog = False

while 1:
    _, shiddy = camera.read()
    shiddy = cv.flip(shiddy, 1)
    shiddyButInGray = cv.cvtColor(shiddy, cv.COLOR_BGR2GRAY)

    face = faceCascade.detectMultiScale(shiddyButInGray, scaleFactor=1.05, minNeighbors=15)

    cv.imshow("god i want to fucking die",shiddy)

    if np.any(face) and not facialRecog:
        facialRecog = True
        #createThread(shiddyButInGray)

    if cv.waitKey(10) == 27:
        break