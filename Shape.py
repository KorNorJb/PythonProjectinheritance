import math
class Shape:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    def area(self):
         S = self.a * self.b
         print(f"Площадь: {S}")
class Rectangle(Shape):
    def area(self):
        S = self.a * self.b
        print(f"Площадь: {S}")
class Circle(Shape):
    def area(self):
         S = math.pi*self.r**2
         print(f"Площадь: {S}")
a = int(input("Введите длину: "))
b = int(input("Введите ширину: "))
r = float(input("Введите радиус: "))
values = Rectangle(a,b,r)
values2 = Circle(a,b,r)
values.area()
values2.area()
