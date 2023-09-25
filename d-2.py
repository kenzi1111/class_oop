# d-2:長方形オブジェクト
# クラスの定義
class Rectangle:
    # 初期設定
    def __init__(self, height, width):
        self.height = height
        self.width = width
    # 面積の計算
    def area(self):
        return self.height * self.width
    #対角線の計算
    def diagonal(self):
        return ((self.height**2) + (self.width**2)) ** 0.5

# 出力ケース１
rectangle1 = Rectangle(height=5, width=6)
area1 = round(rectangle1.area(), 2)
print(area1)  # 30.00
num1 = round(rectangle1.diagonal(), 2)
print(num1)  # 7.81

# 出力ケース2
rectangle2 = Rectangle(height=3, width=3)
area2 = round(rectangle2.area(), 2)
print(area2)  # 9.00
num2 = round(rectangle2.diagonal(), 2)
print(num2)  # 4.24
