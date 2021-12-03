def calc(width, height, *args):

    xMaxL, xMinL, yMaxL, yMinL = args[0]
    xMaxR, xMinR, yMaxR, yMinR = args[1]

    servoXConstL = width / (xMaxL - xMinL)
    servoYConstL = height / (yMaxL - yMinL)

    servoXConstR = width / (xMaxR - xMinR)
    servoYConstR = height / (yMinR - yMaxR)

    return servoXConstL, servoYConstL, servoXConstR, servoYConstR