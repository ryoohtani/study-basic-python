# 課題：３✖️ ３の２次元配列を作成して、５回戦まで行い。選択したインデックスの中身が０ではなく１を当てる。１であれば、勝ち＝＞得点１を加算する。
# ０は負けとする
# ハイスコアは決め打ちで３とする。それを超えた場合はハイスコアの更新を行う
# 間違った場合０を選択していた場合、スコア変数からー１を行う。０以下になった場合は強制的にゲームを終了
# 最後にあなたのスコアを表示させる
# CLIであるシェルのアプリケーションとして作成すること

import random

# 2次元配列の定義
double_list: list = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
# インデックス用変数
x: int = 0
y: int = 0

 # 2次元配列の０初期化
for y in range(len(double_list)):
    for x in range(len(double_list[y])):
        double_list[y][x] =  0


enemy_x: int = random.randint(0, 2)
enemy_y: int = random.randint(0, 2)
double_list[enemy_y][enemy_x] =  '⚪︎'
# 出力して確認するためのテストコード
for i in double_list:
     print(i)

# フラグを下げる
end_flag: bool = False

# フラグが立つまで繰り返す
while end_flag == False: 
    
    err_flag: bool = True
    while err_flag == True:
        i1: str = ''
        i1: str = input('縦軸を決めてください(0〜2)の間で入力してください')
        try:
            i1: int = int(i1)
        except ValueError:
            print('数字を入力してください')
            continue

        if i1 < 0 or 2 < i1:
            print('入力値が不正です。0〜2の間で入力してください。')
            err_flag: bool = True
            continue
        else:
            err_flag: bool = False
            me_y: int = i1
    
    err_flag: bool = True
    while err_flag == True:
        i1: str = ''
        i1: str = input('横軸を決めてください(0〜2)の間で入力してください')
        try:
            i1: int = int(i1)
        except ValueError:
            print('数字を入力してください')
            continue
        
        if i1 < 0 or 2 < i1:
            print('入力値が不正です。0〜2の間で入力してください。')
            err_flag: bool = True
            continue
        else:
            err_flag: bool = False
            me_x: int = i1
    
    err_flag: bool = True
    while err_flag == True:
        last_anser: str = ''
        last_anser: str = input('入力をやり直す場合は、０を入力してください。終了する場合は０以外の数字を入力してください')

        try:
            last_anser: int = int(last_anser)
        except ValueError:
            print('数字を入力してください')
            continue

        if last_anser == 0:
            err_flag: bool = False
            end_flag: bool = False
            continue
        else:
            err_flag: bool = False
            end_flag: bool = True
            double_list[me_y][me_x] = '◻️'
    
# 勝敗の判定
if (enemy_x == me_x) and (enemy_y == me_y):
    print('勝ち')
else:
    print('負け')

# 最終的な結果を出力するコード
for i in double_list:
     print(i)