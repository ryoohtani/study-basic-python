"""
ローカル変数
"""

def show_user_name():
    user_name = "マクレガー"

    print(user_name)

show_user_name()

def total() -> float:
    price1 = 100
    price2 = 200
    tax = 1.1
    return (price1 + price2) * tax

print(total())

"""
グローバル変数
"""
price1 = 100
price2 = 200
tax = 1.1

def total() -> float:
    return price1 + price2 

print(total() * tax)