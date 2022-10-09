
from sympy import Symbol
from sympy.solvers import solve


def evaluate(val):
    x0 = val[0]
    x1 = val[1]
    xmean = val[2]
    y0 = val[3]
    y1 = val[4]
    ymean = val[5]
    radius = val[6]
    m = -(x1 - x0)/(y1 - y0)
    factor_ind = (2*radius)**2 / (1+m**2)
    x = Symbol('x')
    sol_x = solve((x - x0)**2 - factor_ind, x)
    if len(sol_x) == 1:  # Unique solution
        sol_x.append(sol_x[0])
    else:
        pass
    y_1 = m*(sol_x[0]-x0) + y0
    y_2 = m*(sol_x[1]-x0) + y0
    dist1 = ((xmean-sol_x[0])**2
             + (ymean-y_1)**2)**0.5
    dist2 = ((xmean-sol_x[1])**2
             + (ymean-y_2)**2)**0.5
    solution = [sol_x[0], y_1, dist1, sol_x[1], y_2, dist2]
    return solution
