from base64 import encode
import cv2 as cv
import numpy as np
from requests.models import encode_multipart_formdata
import sizematters
import threading
import requests

processFrame = True

def video(cam):
    global processFrame
    t = threading.Timer(2, scuffedCountDown)

    while 1:
        #Captures every frame of the video, processes it and then display it
        _, cum = cam.read()
        cum = cv.flip(cum, 1)
        grayScale = cv.cvtColor(cum, cv.COLOR_BGR2GRAY)
        face = detectFace(grayScale)

        if np.any(face) and processFrame:
            not processFrame
            
            newThread = threading.Thread(target=faceRecog, args=(cum,), daemon=True)
            newThread.start()
        elif not np.any(face) and not processFrame and not t.is_alive():
            t.start()
        elif np.any(face) and not processFrame and t.is_alive():
            t.cancel()

        cv.imshow("shiddy", cum)
        if cv.waitKey(10) == 27:
            break

def detectFace(gray): 
    faceCascade = cv.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
    face = faceCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=15)
    return face

def faceRecog(img):
    params = {
        "api_key": "UN5V5OR6z1c0cqj4k_-HZI8q1DBoEwq0",
        "api_secret": "-jVnsCfNvC-FG_3iGU1WHUMv5O6fIose",
        "face_token1": "a84e77fbbe11cff01cbdaaec4f36f2d9",
    }
    verifyFaceRequest = requests.request(encode_multipart_formdata)

def drawFaceDetections():
    pass

def scuffedCountDown():
    global processFrame
    threading.RLock.acquire()
    if not processFrame:
        processFrame = True
    threading.RLock.release()

# x1 = settings[2][1] + (x / settings[0][0])
# y1 = settings[2][3] - (y / settings[0][1])

# x2 = settings[3][1] + (x / settings[1][0])
# y2 = settings[3][2] + (y / settings[1][1])
# c = np.intc(np.array([x1, y1, x2, y2]))

# coords = f"{c[0]}:{c[1]},{c[2]}:{c[3]}/0\0"

# print(coords)
# port.write(coords.encode())