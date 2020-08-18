x0 = 2448
y0 = 2048
z0 = 710
ovx = 245
ovy = 205
dimx = 2
dimy = 3
umppx0 = 1.43
umppy0 = 1.43
umppz0 = 5.0

xf = 2372
yf = 2956
zf = 606

umppx = None
umppy = None
umppz = None


def calcScaling():

    x1 = (x0 * dimx) - ((dimx - 1) * ovx)
    y1 = (y0 * dimy) - ((dimy - 1) * ovy)
    z1 = z0

    umppx = umppx0 / (xf / x1)
    umppy = umppy0 / (yf / y1)
    umppz = umppz0 / (zf / z1)

    return [umppx, umppy, umppz]

print("um_per_pixel_x,um_per_pixel_y,um_per_pixel_z")
print(calcScaling())
