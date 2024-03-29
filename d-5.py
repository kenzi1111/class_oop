#クラス定義
class MyCounterV2:
    #初期設定：コンストラクタ
    def __init__(self, value,step):
        self.value = value
        self.step = step

    #カウントアップメソッド
    def count_up(self):
        self.value = self.value + self.step
        return  self.value

# 出力
counter1 = MyCounterV2(value=0, step=1)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV2(value=0, step=3)
print(counter2.value)  # 0

counter2.count_up()
print(counter2.value)  # 3

counter2.count_up()
print(counter2.value)  # 6
