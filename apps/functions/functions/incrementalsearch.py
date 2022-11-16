from math import *
import numpy as np


def f(x):
    # evaluate function
    return (np.log(np.sin(x)**2+1)) - 1/2


def incrementalsearch(x0, delta, itermax):
    iteration = 1
    x1 = x0 + delta
    # check if there is a change of sign
    mp = f(x0) * f(x1)

    if mp < 0:
        return(f"The interval entered [{x0}, {x1}] has a root")

    while (iteration <= itermax):

        if mp < 0:
            return(f"There is a root of f in [{x0}, {x1}]")

        x0 = x1
        x1 = x0 + delta
        mp = f(x0) * f(x1)

        iteration = iteration + 1

    if iteration > itermax:
        return "Solution not found, iterations consumed"


# incrementalsearch(-3, 0.5, 100)
