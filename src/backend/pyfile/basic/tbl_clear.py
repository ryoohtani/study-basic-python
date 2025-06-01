double_list: list =  [[3,2,4],
                      [6,1,0],
                      [7,0,2]]

y = 0
x = 0

while y < 3:

    while x < 3:
        if double_list[y][x] != 0:
            double_list[y][x] = 0

        x = x + 1
    
    if x == 3:
        x = 0
    
    y = y + 1

for i in double_list:
    print(i)

print('--------------')

for y in range(len(double_list)): # len関数は２次元配列の行数を取得(lenは組み込み関数)
    # yは行のインデックス
    # xは列のインデックス
    for x in range(len(double_list[y])): # y行目の列数を取得
        if double_list[y][x] != 0:
            double_list[y][x] = 0

for i in double_list:
    print(i) 


# https://www.kaijo-academy.jp/joho/py33.html