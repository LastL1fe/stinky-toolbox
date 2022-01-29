from requests_toolbelt import MultipartEncoder
import requests
import cv2 as cv
from random import randrange
import pprint
import json

# def post():
    # files = {f"{randrange(0, 864846854684684)}": open("temp/temp.png", "rb")}

    # grequests.post("http://76.234.138.246:8000/upload", files=files)


# cam = cv.VideoCapture(0)

# while 1:
#     _, ssSmackMyAss = cam.read()
#     ssSmackMyAss = cv.flip(ssSmackMyAss, 1)

#     cv.imshow("my ass hurt", ssSmackMyAss)

#     if cv.waitKey(10) == 81:
#         newThread = threading.Thread(target=post)
#         cv.imwrite(f"temp/{randrange(0, 9999999999)}.png", ssSmackMyAss)
#         newThread.start()
#     elif cv.waitKey(10) == 27:
#         cv.destroyAllWindows()
#         break

params = {
    "api_key": "UN5V5OR6z1c0cqj4k_-HZI8q1DBoEwq0",
    "api_secret": "-jVnsCfNvC-FG_3iGU1WHUMv5O6fIose",
    "image_url1": "http://76.234.138.246:8000/img/faceass.png"
}

verifyFaceRequest = requests.post(url="https://api-us.faceplusplus.com/facepp/v3/compare", params=params, files={"image_file2": open("temp/temp.png", "rb")})
pp = pprint.PrettyPrinter(depth=6)

pp.pprint(verifyFaceRequest.json())