import math


b = int(input("b >>> "))
a = int(input("a >>> "))
c = int(input("c >>> "))


def equation(a: int, b: int, c:int) -> int or str:
    discriminant = b**2 - a * c * 4
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"x1 = {x1}, x2 = {x2}"
    elif discriminant == 0:
        x = -b / (2 * a)
        return f"x = {x}"
    else:
        return "у уравнения нет корней"

print(equation(a, b , c))