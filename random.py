from microbit import *
import random

sl = 0
while True:
    x = random.randrange(5)
    y = random.randrange(5)
    z = random.randrange(9)+1

    display.set_pixel(x, y, z)

    if button_a.was_pressed():
        if button_b.was_pressed():
            sl = 0
            print(sl)
        sl = sl + 1
        print(sl)
    elif button_b.was_pressed():
        sl = sl - 1
        print(sl)

    if random.randrange(20) == 0:
        if random.randrange(100) == 0:
            sl = 0
            print("RESET")
        change = random.randrange(9) - 4
        sl = sl + change
        print(str(sl) + " - " + str(change))

    sleep(sl)
