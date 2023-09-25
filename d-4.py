#クラス定義
class MyCounterV1:
    #初期設定：コンストラクタ
    def __init__(self, value):
        self.value = value

    #カウントアップメソッド
    def count_up(self):
        self.value = self.value + 1
        return  self.value

# 出力
counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV1(value=7)
print(counter2.value)  # 7

counter2.count_up()
print(counter2.value)  # 8

counter2.count_up()
print(counter2.value)  # 9
