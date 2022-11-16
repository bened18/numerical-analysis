from math import *
import numpy as np


def f(function, x):
    # evaluate function
    #return (np.log(np.sin(x)**2+1)) - 1/2
    return eval(function)


def incrementalsearch(function, x0, delta, itermax):
    
    iteration = 1
    x1 = x0 + delta
    # check if there is a change of sign
    mp = f(function, x0) * f(function, x1)

    if mp < 0:
        return(f"The interval entered [{x0}, {x1}] has a root")

    while (iteration <= itermax):

        if mp < 0:
            return(f"There is a root of f in [{x0}, {x1}]")

        x0 = x1
        x1 = x0 + delta
        mp = f(function, x0) * f(function, x1)

        iteration = iteration + 1

    if iteration > itermax:
        return "Solution not found, iterations consumed"


#print(incrementalsearch('cos(x)', 0, 0.5, 100))
#print (eval('dir()'))
