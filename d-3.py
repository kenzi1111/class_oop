# d-3:正方形オブジェクト

#クラス定義
class Square:
    # 初期設定
    def __init__(self, side):
        self.side = side
    # 正方形の面積の計算
    def area(self):
        return self.side * self.side
    # 正方形の対角線の計算
    def diagonal(self):
        return  (self.side**2 + self.side**2)**0.5
    
# 出力ケース１
square1 = Square(side=1.5)
print(square1.area())  # 2.25
dia1 = round(square1.diagonal(),2)
print(dia1)  # 2.12
# 出力ケース2
square2 = Square(side=15)
print(square2.area())  # 225
dia2 = round(square2.diagonal(),2)
print(dia2)  # 21.21