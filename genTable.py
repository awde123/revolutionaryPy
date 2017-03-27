import math
print("sin(x) = sinx, cos(x) = cosx, tan(x) = tanx")
f = input("f(x): ")
g = input("g(x): ")
ran = input("xMin, xMax: ").split(",")
for x in range(int(ran[0]),int(ran[1]) + 1):
    sinx = math.sin(x)
    cosx = math.cos(x)
    tanx = math.tan(x)
    print(eval(f))
print()
