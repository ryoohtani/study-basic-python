"""
名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。

Humanクラスには、以下の条件で標準出力(print)するcheck_adultメソッドを追加してください。

ageが20以上の場合に大人であること
そうでない場合に大人でないこと
Humanクラスのインスタンスを複数生成してリストに追加し、リストの要素数分だけcheck_adultメソッドを呼び出してください。

本教材で学習した「リスト・タプル」「条件分岐」「繰り返し処理」「関数」「変数のスコープ」「クラス」を用いて、「課題の内容」の仕様通りのプログラムが記述されている
"""

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は{self.age}なので大人です")
        else:
            print(f"{self.name}は{self.age}なので大人ではないです")

human_table = [(5, "マカチェフ"), (10, "ペレイラ"), (15, "ジョーンズ"), (20, "トプリア"), (25, "ベラル")]

for age, name in human_table:
    human_data = Human(age, name)
    human_data.check_adult()


class Human:
    def __init__ (self, age, name):
        self.age = age
        self.name = name
    
    def check_adult(self):
        if 20 <= self.age:
            print(f"{self.name}は{self.age}なので大人です")
        else:
            print(f"{self.name}は{self.age}なので大人ではないです")

ufc_a = Human(5, "マカチェフ")
ufc_b = Human(10, "ペレイラ")
ufc_c = Human(15, "ジョーンズ")
ufc_d = Human(20, "トプリア")
ufc_e = Human(25, "ベラル")

Human_table = [ufc_a, ufc_b, ufc_c, ufc_d, ufc_e]

for i in Human_table:
    i.check_adult()