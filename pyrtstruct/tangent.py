def tangent(vector, cont):
    # The value +2 is selected due to it is.
    # Recommended to evaluate the slope locally.
    # Ergo, near to the initial point. +1 is not.
    # Recommeded due to many slopes will be zero of.
    # Infinity. +3 can produces higher changes in slopes.
    length = int(len(vector)/3)
    x0 = vector[3*cont]
    y0 = vector[3*cont + 1]
    if cont >= (length-8):
        x1 = vector[3]
        y1 = vector[4]
    else:
        x1 = vector[3*cont + 6]
        y1 = vector[3*cont + 7]
    coord = [x0, y0, x1, y1]
    return coord
