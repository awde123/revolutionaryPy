import math
from math import sin, cos, tan, exp, sqrt

fVal = []
gVal = []
xVal = []

f = eval("lambda x: {0}".format(input("f(x): ")))
g = eval("lambda x: {0}".format(input("g(x): ")))
x = min = float(input("x min: "))
max = float(input("x max: "))
delx = float(input("delta x: "))
delta = .000001

while x <= max:
    fVal += [f(x)]
    gVal += [g(x)]
    xVal += [x]
    x += delx

def cfunc(x):
    return (f(x) - g(x))

def cderiv(x):
    return (cfunc(x+delta)-cfunc(x)) / delta

def rt(guess=2, trials=12, func=cfunc, deriv=cderiv):
    for i in range(0, trials):
        guess = guess - (func(guess)/deriv(guess))
    return guess

int1 = rt(guess=min, trials=20)
int2 = rt(guess=max, trials=20)

fVal += [f(int1), f(int2)]
gVal += [g(int1), g(int2)]
xVal += [int1, int2]

fFile = open('f','w')
gFile = open('g','w')
xFile = open('x','w') ## illuminati confirmed

fFile.write(str(fVal))
gFile.write(str(gVal))
xFile.write(str(xVal))
