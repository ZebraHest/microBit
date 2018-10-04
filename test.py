
x = (1, 0, 0.1)
y = (0, 1, 0.1)

z = (x[1]*y[2] - x[2]*y[1],
     x[0] * y[2] - x[2] * y[0],
     x[0] * y[1] - x[1] * y[0])

print(z)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[0] * b[2] - a[2] * b[0],
            a[0] * b[1] - a[1] * b[0])


print(cross(x, y))
