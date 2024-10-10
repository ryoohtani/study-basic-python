# :intとは引数の型ヒントのこと(明示的にわかりやすくするため)
# -> boolは、戻り値の型ヒント。戻り値に対して型を明示的に示している
def add_keisan(a, b: int) -> int:
    result = (a + b) * 2
    return result

last_result = add_keisan(5, 3)
print(last_result)


############## 下記別のプログラム ##############

# 購入判定フラグ (Trueなら出力)
kounyuu_flag = True

# 戻り値の結果をみて、どのような処理にするか？についての定義を記載
# -> boolは、戻り値の型ヒント。戻り値に対して型を明示的に示している
def shop_konyuu_zumi() -> bool:
    if (kounyuu_flag): # 真
        return True
    else:              # 偽
        return False

# 処理の結果下記、関数名の戻り値の値がTrueなら出力される
if (shop_konyuu_zumi() == True):
    print("購入済みです")