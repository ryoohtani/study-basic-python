import random
num = random.randint(1, 4)

if 1 < num and num < 3:
    print("変数numは1より大きく、3より小さいです▶", num)
elif num == 3:
    print("numは3なので当たりです▶", num)
else:
    print("ハズレです▶️", num)