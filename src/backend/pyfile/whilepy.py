# ゴール → 合計金額が２０を超えるまで、中身の金額を知りたい
# 注意点としては、ランダム生成に使用している変数numに格納される数字が２で割り切れる数字なら加算処理を行わない
# sum変数を使用すること(金額合計用の変数→値が２０以上になったら処理を終了させる)
# numの変数を用意して、１から１０までのランダムの数字取り扱えるようにすること、偶数で割り切れる判定用に必要

import random

sum = 0

while sum < 20:
    # １から１０までのランダムの数字を、numの変数に格納していく
    num = random.randint(1, 10)
    print('現在のnumの値は', num)

    if num % 2 == 0:
        continue

    sum = sum + num
    print(sum)