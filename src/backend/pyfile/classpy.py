""" クラスの基本構文 """
# クラスの定義
class Product:
    クラスの特徴(属性)
# インスタンス化する
coffee = Product()
# クラス名は慣習的に先頭を大文字にします



""" 属性 """
# 属性の基本構文
# クラスの定義
class Product:
    #コンストラクタ
    def __init__(self): 
        # 属性を定義
        self.name = ""
        self.price = 0
# インスタンス化する
coffee = Product()
# 属性にアクセスし、値を代入する
coffee.name = "エスプレッソ"
coffee.price = 120
print(coffee.name, coffee.price)



""" メソッド """
# クラスの定義
class Product:
    # コンストラクタ
    def __init__(self): 
        # 属性を定義
        self.name = ""

    # メソッドの定義
    def set_name(self, name):
        self.name = name

    # メソッドから名前の表示
    def show_name(self):
        print(self.name)
# インスタンス化する
coffee = Product()
# メソッドにアクセスして実行する
coffee.set_name("エスプレッソ")
# 名前の表示するメソッドにアクセス
coffee.show_name()



""" コンストラクタ """
class Drink:
    # コンストラクタを定義する
    def __init__(self, name, price, country):
        # 属性を定義する
        self.name = name
        self.price = price
        self.country = country 

    # メソッドから名前の表示
    def show_name(self):
        print(self.name)
        print(self.price)
        print(self.country)
# インスタンス化
coffee = Drink("エスプレッソ", 120, "ブラジル")
# 属性にアクセスし、値を出力する
coffee.show_name()



""" クラスの全体的な基本構文 """

# クラスの定義（例：class Product: ...... ）
class クラス名:
    # コンストラクタの定義
    def __init__(self):
        初期化の内容

    # メソッドの定義（例：public show_name(): ...... ）
    def メソッド名():
        一連の処理
# インスタンス化（例：shampoo = Product()）
インスタンス名 = クラス名()
# 属性へのアクセス（例：shampoo.name）
インスタンス名.属性名
# メソッドへのアクセス（例：shampoo.show_name()）
インスタンス名.メソッド名()



class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name)
        print(self.age)

a_human = Human("日本太郎", 50)
a_human.printinfo()