import math
from math import sin, cos, tan, exp, sqrt

pi = 3.14159265359
e = 2.71828182846

fVal = gVal = xVal = iVal = xiVal = []

f = eval("lambda x: {0}".format(input("f(x): ")))
g = eval("lambda x: {0}".format(input("g(x): ")))
x = min = float(input("x min: "))
max = float(input("x max: "))
delx = float(input("delta x: "))
delta = .000001

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

print("intersection computation complete")

while x <= max:
   if x <= int1 or x >= int2:
       fVal += [f(x)]
       gVal += [g(x)]
       xVal += [x]
   x += delx

print("non-intersection complete")

x = int1
while x < int2:
    iVal += [f(x)]
    xiVal += [x]
    iVal += [g(x)]
    xiVal += [x]
    x += delx

print("intersection complete")

fVal += [f(int1), f(int2)]
gVal += [g(int1), g(int2)]
xVal += [int1, int2]

print(fVal)
print(gVal)
print(xVal)

open('f','w').write(str(fVal).replace("[","").replace("]",""))
open('g','w').write(str(gVal).replace("[","").replace("]",""))
open('x','w').write(str(xVal).replace("[","").replace("]",""))
open('i','w').write(str(iVal).replace("[","").replace("]",""))
open('xi','w').write(str(xiVal).replace("[","").replace("]",""))
