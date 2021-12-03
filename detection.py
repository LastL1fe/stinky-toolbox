import cv2
import numpy as np

def detectFace(img, gray, port, val, *settings): 

    faceCas = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    face = faceCas.detectMultiScale(gray, 1.07, 7, minSize = [30, 30])

    fire = False

    for (x, y, w, h) in face:

        if not val: fire = True

        coords = ""
        
        if not val:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "victim", (x, y+30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 1)
        elif val:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "jar", (x, y+30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)

        x1 = settings[2][1] + (x / settings[0][0])
        y1 = settings[2][3] - (y / settings[0][1])

        x2 = settings[3][1] + (x / settings[1][0])
        y2 = settings[3][2] + (y / settings[1][1])

        c = np.intc(np.array([x1, y1, x2, y2]))

        coords = f"{c[0]}:{c[1]},{c[2]}:{c[3]}/{int(fire)}\0"
        
        print(coords)
        port.write(coords.encode())