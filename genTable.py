## library importation and constant defintion for user use
from math import sin, cos, tan, exp, sqrt
pi = 3.14159265359
e = 2.71828182846

## initial variable declaration
fVal = []
gVal = []
xVal = []
iVal = []
xiVal = []

## user inputs python code to be used as function
f = eval("lambda x: {0}".format(input("f(x): ")))
g = eval("lambda x: {0}".format(input("g(x): ")))
## user defines bounds and delta
x = min = float(input("x min: "))
max = float(input("x max: "))
delx = float(input("delta x: "))
## delta for derivative calculation
delta = .000001

## Newton's method:
## function which subtracts user inputted equations for newton's method
def cfunc(x):
    return (f(x) - g(x))
## finds derivative with previously defined delta
def cderiv(x):
    return (cfunc(x+delta)-cfunc(x)) / delta
## newton's method, finds intersect of two equations
def rt(guess=2, trials=12, func=cfunc, deriv=cderiv):
    for i in range(0, trials):
        guess = guess - (func(guess)/deriv(guess))
    return guess

## defines two intersects
int1 = rt(guess=min, trials=20)
int2 = rt(guess=max, trials=20)

## finds y values when functions are not intersecting yet
while x <= max:
   if x <= int1 or x >= int2:
       fVal += [f(x)]
       gVal += [g(x)]
       xVal += [x]
   x += delx

## finds y values when functions are intersecting (for solid)
x = int1
while x < int2:
    iVal += [f(x)]
    xiVal += [x]
    iVal += [g(x)]
    xiVal += [x]
    x += delx

## adds final coordinate to f and g lists
fVal += [f(int1), f(int2)]
gVal += [g(int1), g(int2)]
xVal += [int1, int2]


## exports data
open('f.coord','w').write(str(fVal).replace("[","").replace("]",""))
open('g.coord','w').write(str(gVal).replace("[","").replace("]",""))
open('x.coord','w').write(str(xVal).replace("[","").replace("]",""))
open('i.coord','w').write(str(iVal).replace("[","").replace("]",""))
open('xi.coord','w').write(str(xiVal).replace("[","").replace("]",""))
