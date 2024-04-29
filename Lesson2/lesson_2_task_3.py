import math

def square(a):
    return a * a

lenght = 5.1
area = square(lenght)
rounded = math.ceil(area) 
print("площадь:", area, "округлённо:", rounded) 

# from math import ceil

# def sqr(a):
    # return ceil(a*a)

# print(sqr (5.01))
# print(sqr (5))
# print(5.01*5.01)
