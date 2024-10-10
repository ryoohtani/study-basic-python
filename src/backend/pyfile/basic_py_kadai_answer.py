"""
名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。

Humanクラスには、以下の条件で標準出力(print)するcheck_adultメソッドを追加してください。

ageが20以上の場合に大人であること
そうでない場合に大人でないこと
Humanクラスのインスタンスを複数生成してリストに追加し、リストの要素数分だけcheck_adultメソッドを呼び出してください。

本教材で学習した「リスト・ディクショナリ」「条件分岐」「繰り返し処理」「関数」「変数のスコープ」「クラス」を用いて、「課題の内容」の仕様通りのプログラムが記述されている
"""

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です。")
        else:
            print(f"{self.name}は子供です。")
            

human_list = [(10, "トム"),(15, "ボブ"),(20, "サム"),(25, "ナム"),(30, "ハム")]

for age, name in human_list:
    Human_instans = Human(age, name)
    Human_instans.check_adult()