import serial as s
import time

port = s.Serial(port = 'COM3', baudrate = 9600)
time.sleep(1)

coords = "1"

port.write(coords.encode())