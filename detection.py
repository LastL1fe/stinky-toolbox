import asyncio
import aiohttp
import cv2 as cv
import numpy as np
import threading
import requests

processFrame = True
confidence = None

def video(cam, port, leftServoCal, rightServoCal, consts):
    global processFrame

    faceCascade = cv.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
    newTimerCreation = True
    currentTimer = None

    while 1:
        #Captures every frame of the video, processes it and then display it
        _, cum = cam.read()
        cum = cv.flip(cum, 1)
        grayScale = cv.cvtColor(cum, cv.COLOR_BGR2GRAY)
        face = detectFace(grayScale, faceCascade)

        if np.any(face) and processFrame: 
            processFrame = False
            saveFace(face, cum)
            #logFace()
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            asyncio.run(faceRecog())
        elif not np.any(face) and not processFrame and newTimerCreation and currentTimer == None:
            newTimerCreation = False
            t = threading.Timer(1 , scuffedCountDown)
            t.start()
            currentTimer = t  
        elif np.any(face) and not processFrame and not newTimerCreation and currentTimer != None:
            currentTimer.cancel()
            currentTimer = None
            newTimerCreation = True
        elif np.any(face) and not processFrame:
            if not confidence: pass 
            else: drawFaceDetections(face, cum, confidence > 100, port, leftServoCal, rightServoCal, consts)

        if cv.waitKey(33) == 27:
            port.write("90:90,90:90/0\0".encode())
            break

        cv.imshow("shiddy", cum)

def detectFace(gray, faceCascade):
    face = faceCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=6)
    return face

def saveFace(face, img):
    for (x, y, w, h) in face:
        img = img[y:y+h, x:x+w]
        cv.imwrite("temp/temp.png", img)

async def faceRecog():
    global confidence
    global processFrame
    async with aiohttp.ClientSession() as bussy:
        url = "https://api-us.faceplusplus.com/facepp/v3/compare"
        params = {
            "api_key": "UN5V5OR6z1c0cqj4k_-HZI8q1DBoEwq0",
            "api_secret": "-jVnsCfNvC-FG_3iGU1WHUMv5O6fIose",
            "image_url1": "http://76.234.138.246:8000/img/faceass.png",
            "image_file2": open("temp/temp.png", "rb")
        }

        async with bussy.post(url=url, data=params) as res:
            result = await res.json()
            
            try:
                print(result)
                confidence = result["confidence"]
            except KeyError:
                processFrame = True

def logFace():
    url = "http://76.234.138.246:8000/upload"
    files = {"image_file2": open("temp/temp.png", "rb")}
    requests.post(url=url, files=files)
    
def scuffedCountDown():
    global processFrame
    lock = threading.Lock()
    if not processFrame:
        lock.acquire()
        processFrame = True
        lock.release()
        print("released")

def drawFaceDetections(face, cum, confidence, port, leftServoCal, rightServoCal, consts):
    if confidence:
        for (x,y,w,h) in face:
            cv.rectangle(cum, (x, y), (x+w, y+h), (0, 255, 0), 2)
        firePort(port, int(confidence)-1, leftServoCal, rightServoCal, consts, (x, y))
    else:
        for (x,y,w,h) in face:
            cv.rectangle(cum, (x, y), (x+w, y+h), (0, 0, 255), 2)

        firePort(port, int(confidence)+1, leftServoCal, rightServoCal, consts, (x, y))

def firePort(port, confidence, leftServoCal, rightServoCal, consts, coords):
    #settings
    x, y = coords
    xRight, xLeft, yTop, yBot = leftServoCal
    xRight2, xLeft2, yTop2, yBot2 = rightServoCal
    x1Const, y1Const, x2Const, y2Const = consts

    #print("working")

    x1 = xLeft + (x / x1Const)
    y1 = yTop + (y / y1Const)

    x2 = xLeft2 + (x / x2Const)
    y2 = yTop2 - (y / y2Const)
    c = np.intc(np.array([x1, y1, x2, y2]))

    coords = f"{c[0]}:{c[1]},{c[2]}:{c[3]}/{confidence}\0"

    print(coords)
    port.write(coords.encode())