x0 = 2448
y0 = 2048
z0 = int(input("z0: "))
ovx = 245
ovy = 205
dimx = int(input("dimx: "))
dimy = int(input("dimy: "))
umppx0 = 1.43
umppy0 = 1.43
umppz0 = 5.0

xf = int(input("xf: "))
yf = int(input("yf: "))
zf = int(input("zf: "))

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

with open('stitched_scaling.csv', 'w') as f:
    f.write(str(calcScaling()) + "\n")
