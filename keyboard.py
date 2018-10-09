from microbit import *
import math

threshold = 150
letters = (("a", "b", "c", "d", "e"),
           ("f", "g", "h", "i", "j"),
           ("k", "l", "m", "n", "o"),
           ("p", "q", "r", "s", "t"),
           ("u", "v", "x", "y", "z"))

def show_dot():
    x_acc = accelerometer.get_x()
    y_acc = accelerometer.get_y()

    x_acc = min(x_acc, 2 * threshold)
    y_acc = min(y_acc, 2 * threshold)

    x_acc = max(x_acc, -2 * threshold)
    y_acc = max(y_acc, -2 * threshold)

    x_pos = 0
    y_pos = 0

    if x_acc != 0:
        x_pos = math.floor(x_acc / threshold)

    if y_acc != 0:
        y_pos = math.floor(y_acc / threshold)

    #print(x_pos, y_pos)
    x_pos = x_pos + 2
    y_pos = y_pos + 2

    display.clear()
    display.set_pixel(x_pos, y_pos, 9)
    return x_pos, y_pos


def print_dot(x_pos, y_pos):
    if button_a.was_pressed() | button_b.was_pressed():
        print(letters[y_pos][x_pos])


def main():
    while True:
        x_pos, y_pos = show_dot()
        print_dot(x_pos, y_pos)
        sleep(10)


main()
