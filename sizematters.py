import cv2 as cv


def resize(frame, scale = .75):
    #works with any media, not optimal for videos
    length = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (length, width)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


def rez(video, width, height):
    #only works for live video
    #dont be a dumbass
    newWindow = video.set(3, width),  video.set(4, height) #ID 4 Height
    return newWindow