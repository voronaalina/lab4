import math
def calc_Z(x, y, a, t):
    #обчислимо 1 частину
    elem1 = x*math.sin(y)
    elem2 = y*math.cos(a)
    elem3 = 2.33*math.pi*(elem1+elem2)
    #обчислимо 1 і 2 частину
    Z = elem3 + math.exp(a*t)
    return Z
x = float(input("введіть x:"))
y = float(input("введіть y:"))
a = float(input("введіть a:"))
t = float(input("введіть t:"))
result = calc_Z(x, y, a, t)
print("Z=", result)