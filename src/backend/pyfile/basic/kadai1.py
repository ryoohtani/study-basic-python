# 課題：３✖️ ３の２次元配列を作成して、５回戦まで行い。選択したインデックスの中身が０ではなく１を当てる。１であれば、勝ち＝＞得点１を加算する。
# ０は負けとする
# ハイスコアは決め打ちで３とする。それを超えた場合はハイスコアの更新を行う
# 間違った場合０を選択していた場合、スコア変数からー１を行う。０以下になった場合は強制的にゲームを終了
# 最後にあなたのスコアを表示させる
# CLIであるシェルのアプリケーションとして作成すること

import random
# スコア変数の定義
score: int = 3
high_score: int = 2

def clear_func():
    # インデックス用変数定義
    x: int = 0
    y: int = 0
    # 2次元配列の定義
    double_list: list = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]

    # 2次元配列の０初期化
    for y in range(len(double_list)):
        for x in range(len(double_list[y])):
            double_list[y][x] =  0
    
    return double_list

def enemy_func(double_list: list):
    # 敵のインデックスをランダムで決定０から２まで
    enemy_x: int = random.randint(0, 2)
    enemy_y: int = random.randint(0, 2)
    double_list[enemy_y][enemy_x] =  '⚪︎'

    return enemy_x, enemy_y, double_list

def hint_func(enemy_x: int):
    print('ヒントが欲しい場合は、「y」を入力してください。')
    hint_flag: str = input('ヒントを表示しますか？(y/n): ')
    if hint_flag == 'y':
        print(f'敵の横の座標は{enemy_x}です。')

def player_func(get_xy_text: str):
    i1: str = ''
    err_flag: bool = True

    while err_flag == True:
        i1: str = input(f'{get_xy_text}軸を決めてください(0〜2)の間で入力してください:')
        try:
            i1: int = int(i1)
        except ValueError:
            print('数字を入力してください')
            err_flag: bool = True
            continue

        if i1 < 0 or 2 < i1:
            print('入力値が不正です。0〜2の間で入力してください。')
            err_flag: bool = True
            continue

        last_anser: str = ''
        last_anser: str = input('入力をやり直す場合は、０を入力してください。終了する場合は０以外の数字を入力してください')
        try:
            last_anser: int = int(last_anser)
        except ValueError:
            print('数字を入力してください')
            err_flag: bool = True
            continue

        if last_anser == 0:
            err_flag: bool = True
            continue
        else:
            err_flag: bool = False
            return i1       
            
def main():
    global score, high_score
    game_flag: bool = True
    while game_flag == True:
        double_list = clear_func()
        print('現在のハイスコア' + str(high_score) + 'です')
        print('$$$$$ ゲーム開始 $$$$$')
        enemy_x, enemy_y, double_list = enemy_func(double_list)
        hint_func(enemy_x)
        me_y = player_func('縦')
        me_x = player_func('横')
        double_list[me_y][me_x] = '◻️'

        # 勝敗の判定
        if (enemy_x == me_x) and (enemy_y == me_y):
            score = score + 1
            print('勝ちました' + str(score) + '点')
        else:
            score = score - 1
            print('負け' + str(score) + '点')
        
        if score > high_score:
            high_score = score
            print('ハイスコアを更新しました！' + str(high_score) + '点')
            print('#################')

        # 最終的な結果を出力するコード
        for i in double_list:
            print(' '.join(str(i2) for i2 in i))
        print('#################')

        print('あなたのスコアは' + str(score) + 'です。')
    
        if score < 0:
            print('ゲームオーバーです。')
            game_flag = False
            break
        else:
            continue_flag: str = input('続ける場合は「y」を入力してください。終了する場合は「n」を入力してください:')
            if continue_flag == 'y':
                game_flag = True
            else:
                game_flag = False
                print('ゲームを終了します。')
                break

#def textwrite():
    #print('ゲームの結果をファイルに書き込みます。')

if __name__ == "__main__":
    main()

#textwrite()