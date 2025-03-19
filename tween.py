import numpy as np

FPS = 30

def linear(x):
    return x

def easeInQuad(x):
    return x**2

def easeOutQuad(x):
    return 1-(1-x)**2

def easeInOutQuad(x):
    if x < 0.5:
        return 2*x**2
    else:
        return 1-(2*(1-x)**2)

def easeInCubic(x):
    return x**3

def easeOutCubic(x):
    return 1-(1-x)**3

def easeInOutCubic(x):
    if x < 0.5:
        return 4*x**3
    else:
        return 1-(2*(1-x)**3)

def tween(duration: float, func, mapping=linear):
    for x in np.linspace(0, 1, num=int(duration*FPS+1)):
        yield func(mapping(x))

