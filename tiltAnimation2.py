from microbit import *
import math

maximum = 512
minimum = -maximum


def set_corners():
    x_reading = accelerometer.get_x()
    y_reading = accelerometer.get_y()

    x_reading = min(x_reading, maximum)
    x_reading = max(x_reading, minimum)
    x_reading = x_reading / maximum

    y_reading = min(y_reading, maximum)
    y_reading = max(y_reading, minimum)
    y_reading = y_reading / maximum

    for i in range(-2, 3):
        for j in range(-2, 3):
            set_corner(i, j, x_reading, y_reading)

    if button_b.is_pressed():
        show()


def set_corner(x_pos, y_pos, x_reading, y_reading):
    normal = cross((1, 0, x_reading), (0, -1, y_reading))

    #norm_factor = math.sqrt(normal[0] * normal[0] + normal[1] * normal[1] + normal[2] * normal[2])
    #normal = (normal[0] * norm_factor, normal[1] * norm_factor, normal[2] * norm_factor)

    z = (-normal[0] * x_pos - normal[1] * y_pos) / normal[2]

    threshold = 2.3

    z = (z + threshold) / (2 * threshold)
    z = min(z, 1)
    z = max(0, z)
    z = z * 9
    z = math.ceil(z)

    if button_a.is_pressed():
        print(z)

    display.set_pixel(x_pos + 2, y_pos + 2, z)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[0] * b[2] - a[2] * b[0],
            a[0] * b[1] - a[1] * b[0])


def show():
    for i in range(0, 5):
        h = ""
        for j in range(0, 5):
            h = h + str(display.get_pixel(j, i))
        print(h)
    print("")
    sleep(1000)


def main():
    while True:
        set_corners()


main()
