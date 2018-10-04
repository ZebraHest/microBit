from microbit import *


def to_string(i):
    num = i % 17
    if num > 8:
        num = (16 - num) % 9
    return str(num + 1)


def make_line(i):
    return (to_string(i + 0) +
            to_string(i + 1) +
            to_string(i + 2) +
            to_string(i + 3) +
            to_string(i + 4) + ':')


def make_screen(i):
    return Image(make_line(i + 0) +
                 make_line(i + 1) +
                 make_line(i + 2) +
                 make_line(i + 3) +
                 make_line(i + 4))


k = 0
while True:
    show = make_screen(k)
    display.show(show)
    k = k + 1
    sleep(1)
    while button_a.is_pressed():
        sleep(1)
