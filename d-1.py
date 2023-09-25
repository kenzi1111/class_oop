# 課題D-1:円オブジェクト


# クラスの定義
class Circle:
    #
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14

    def perimeter(self):
        return (self.radius * 2) * 3.14


# 半径が1
circle1 = Circle(radius=1)
print(circle1.area())
print(circle1.perimeter())

# 半径が3
circle3 = Circle(radius=3)
print(circle3.area())
print(circle3.perimeter())
