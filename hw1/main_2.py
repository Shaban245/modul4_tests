import math

a = float(input("a >> "))
b = float(input("b >> "))
c = float(input("c >> "))

def triangle_area(a: float, b: float, c: float ) -> str:
    if (a+b > c) and (a+c > b) and (b+c > a):
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c) )
        return area
    else:
        return "такого треугольника не существует"

print(triangle_area(a, b, c))