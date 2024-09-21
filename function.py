import math
def calc_func(x):
    chyselnyk = math.exp(x**2)
    znamennyk = math.cos(x+x**4)
    elem1 = chyselnyk/znamennyk 
    elem2 = (x+x**3)**(1/4)

    return elem1 - elem2
x=float(input("введіть х:"))
result = calc_func(x)
print("f(x)=", result)