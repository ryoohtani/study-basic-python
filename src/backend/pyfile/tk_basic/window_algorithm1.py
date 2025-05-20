import sys

# 例題563201、7802、19805243の整数がある。それらの千の位の数を、変数tに代入して出力するアルゴリズムを作成してください

# 1つ目のパターン。文字列にしてから文字列操作を行い１０００の位を取得する
i1 = 563201
i2 = 7802
i3 = 19805243
moji_right = 4

s1 = str(i1)
s2 = str(i2)
s3 = str(i3)

if len(s1) < moji_right or len(s2) < moji_right or len(s3) < moji_right:
    print("1000桁以上の値のみ有効")
    sys.exit()

print(s1[-moji_right:])
print(s2[-moji_right:])
print(s3[-moji_right:])

# 整数に戻す方法
i1 = s1[-moji_right:]
i2 = s2[-moji_right:]
i3 = s3[-moji_right:]

print(int(i1))
print(int(i2))
print(int(i3))

# 2つ目のパターン。整数の割り算を使って千の位を取得する
print("-----------------")
i1 = 563201
i2 = 7802
i3 = 19805243
