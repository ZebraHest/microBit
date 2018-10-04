from microbit import *

while True:
    reading = accelerometer.get_gestures()
    print(str(reading))
    sleep(100)
