from math import sqrt

from Variables import result


def greet():
    print("Hello, functions")


def area_circle(radius):
    result = 22 / 7 * radius ** 2
    result = round(result, 2)
    print(result)


def volume_cylinder(h, r, precision=2):
    v = 22 / 7 * r ** 2 * h
    v = round(v, precision)
    print(f" Radius is {r}, Height is {h} ,volume is {v}")


def area_of_triangle(a, b, c):
    """"calculates the area of the triangle then returns the result"""
    s = (a + b + c) / 2
    A = sqrt(s * (s - a) * (s - b) * (s - c))
    print(A)
    return A


# 4== 4*3*2*1
def factorial(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result


def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result


# function that if i give cash ksh3000
def clean_numbers(word)
    return result


print(clean_numbers("ksh6000"))  # 6000

print(add_numbers(2, 5))
print(add_numbers(2, 5, 7, 1))
# print(factorial(4))
# use a function== call function

# area_of_triangle(10,10,10)


# volume_cylinder(10,10,3)
# volume_cylinder(16,10,5)
# volume_cylinder(5,10,2)
# volume_cylinder(r=45, h=67, precision=2)# named params


# area_circle(7)
# area_circle(25)
# area_circle(7.5654)


# greet()
# greet()
# greet()
