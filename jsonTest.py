import json

def shatMyself(*args):
    xMax, xMin, yMax, yMin = args[0]

    print(xMax, xMin, yMax, yMin)
    

with open("calibration.json", "r") as calibration:
    settings = json.load(calibration)

shatMyself(tuple(settings['Left Servos Calibration'].values()))