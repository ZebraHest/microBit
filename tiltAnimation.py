from microbit import *
import math

threshold = 20
maximum = 512
minimum = -maximum


def get_single(x_pos, y_pos, x_reading, y_reading):
    x_reading = min(x_reading, maximum)
    x_reading = max(x_reading, minimum)

    y_reading = min(y_reading, maximum)
    y_reading = max(y_reading, minimum)

    # y_value = 5 + math.ceil(y_reading / maximum * y_pos * 2)

    x_value = abs(x_reading / maximum)
    y_value = abs(y_reading / maximum)

    value = x_value + y_value

    value = min(value, 4/3)

    return str(math.ceil(value * 2/3 * 9))


def get_line(y_pos, x_reading, y_reading):
    return (get_single(-2, y_pos, x_reading, y_reading) +
            get_single(-1, y_pos, x_reading, y_reading) +
            get_single(0, y_pos, x_reading, y_reading) +
            get_single(1, y_pos, x_reading, y_reading) +
            get_single(2, y_pos, x_reading, y_reading) + ":")


def create_screen(x_reading, y_reading):
    string = (get_line(-2, x_reading, y_reading) +
              get_line(-1, x_reading, y_reading) +
              get_line(0, x_reading, y_reading) +
              get_line(1, x_reading, y_reading) +
              get_line(2, x_reading, y_reading))
    print(string)
    return Image(string)


def main():
    while True:
        x_reading = accelerometer.get_x()
        y_reading = accelerometer.get_y()

        display.show(create_screen(x_reading, y_reading))


main()
