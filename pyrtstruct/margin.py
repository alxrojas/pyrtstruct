
import numpy as np

import evaluate
import tangent


def margin(agenda, radius, expand=True):
    # Function that calculates the expanded contour for each point.
    # Of old contour. The algorithm uses the maximum displacement.
    # The algorithm works as follows:
    # 1. The point p0 and the next (p1) of the contour are taken.
    # For the i-th slice.
    # 2. The slope of the tangent line (T) at that point p0 of the.
    # Contour (C) is calculated.
    # 3. The x-coordinate of po is calculated. For this, the point.
    # That intercepts T, a circumference of radius r and a normal.
    # Line (N) to T is considered. For which the quadratic equation.
    # Is solved: (x-x0)^2 - factor_ind = 0.
    # 4. There are two solutions: one of them is the optimal one,
    # Which has the property.
    # Of being outside C. For this, both solutions are evaluated.
    # Taking the Euclidean distance between these points and the.
    # Mean coordinates of the contour (center of mass).
    # The one with the greatest distance is the one we are looking.
    # INPUT:
    # Agenda -> dict, the structures
    # Radius -> float, Margin for expansion
    # expand -> bool, True if expand. False if contract
    # OUTPUT:
    # Structures -> dict, with the coordinates with the extension.
    structures = {}
    for mets in agenda:
        contours = []
        for slices in range(len(agenda[mets])):
            x, y, array = [], [], []
            vector = agenda[mets][slices]
            length = int(len(vector)/3)
            for count in range(length):
                x.append(vector[3*count])
                y.append(vector[3*count + 1])
            xmean = (max(x) + min(x))/2
            ymean = (max(y) + min(y))/2
            for cont in range(length):
                x0, y0, x1, y1 = tangent.tangent(vector, cont)
                if (x0 != x1) and (y0 != y1):
                    val = [x0, x1, y0, y1, xmean, ymean, radius]
                    x1_s, y_1, dist1, x2_s, y_2, dist2 = evaluate.evaluate(val)
                    if expand:
                        if dist1 > dist2:
                            array.append(x1_s)
                            array.append(y_1)
                        else:
                            array.append(x2_s)
                            array.append(y_2)
                    else:
                        if dist1 < dist2:
                            array.append(x1_s)
                            array.append(y_1)
                        else:
                            array.append(x2_s)
                            array.append(y_2)
                else:
                    if expand:
                        if x0 > xmean:
                            array.append(x0 + radius)
                        else:
                            array.append(x0 - radius)
                        if y0 > ymean:
                            array.append(y0 + radius)
                        else:
                            array.append(y0 - radius)
                    else:
                        if x0 > xmean:
                            array.append(x0 - radius)
                        else:
                            array.append(x0 + radius)
                        if y0 > ymean:
                            array.append(y0 - radius)
                        else:
                            array.append(y0 + radius)
                array.append(float(vector[3*cont + 2]))
            contours.append(list(np.transpose(array)))
        structures[mets] = contours
    return structures
