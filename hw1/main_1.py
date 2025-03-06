import math

def equation(a: int, b: int, c:int) -> int or str:
    discriminant = b**2 - a * c * 4
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return print("у уравнения нет корней")
