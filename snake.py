from microbit import *
import random
import math

threshold = 1


def update_array(array, pos):
    array = list(array)
    for i in range(0, len(array)-1):
        array[i] = array[i+1]
    array[len(array)-1] = pos
    return array


def update_pos(pos):
    x_pos = pos[0]
    y_pos = pos[1]

    x_acc = accelerometer.get_x()
    y_acc = accelerometer.get_y()

    if abs(x_acc) > abs(y_acc):
        if x_acc > threshold:
            x_pos += 1
        elif x_acc < - threshold:
            x_pos -= 1
    else:
        if y_acc > threshold:
            y_pos += 1
        elif y_acc < -threshold:
            y_pos -= 1

    x_pos = x_pos % 5
    y_pos = y_pos % 5
    return x_pos, y_pos


def print_snake(array, dot_pos):
    display.clear()
    for i in range(0, len(array)):
        brightness = 7-math.floor((len(array)-i-1)/len(array) * 5)
        print(brightness)
        display.set_pixel(array[i][0], array[i][1], brightness)
    display.set_pixel(dot_pos[0], dot_pos[1], 9)


def check_pos(pos, array):
    for ar in array:
        if ar == pos:
            while True:
                display.show(Image.ANGRY, clear=True)
                sleep(500)
                display.scroll(len(array))
                sleep(500)


def handle_dot(array, pos, dot_pos):
    if pos == dot_pos:
        array.insert(0, dot_pos)
        return create_random_dot(array)
    return dot_pos


def create_random_dot(array):

    good_spot = False

    while not good_spot:
        x_pos = random.randrange(0, 5)
        y_pos = random.randrange(0, 5)
        pos = (x_pos, y_pos)
        good_spot = True
        for ar in array:
            if ar == pos:
                good_spot = False

    display.set_pixel(x_pos, y_pos, 9)
    return x_pos, y_pos


def main():
    array = [(2, 2)]
    dot_pos = create_random_dot(array)
    pos = (2, 2)
    while True:
        pos = update_pos(pos)
        check_pos(pos, array)
        dot_pos = handle_dot(array, pos, dot_pos)
        array = update_array(array, pos)
        print_snake(array, dot_pos)
        speedup = math.floor(500 * (len(array) / 10))
        speedup = min(700, speedup)
        sleep(1000 - speedup)


main()
