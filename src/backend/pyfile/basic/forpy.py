import random

for i in range(1, 11):
  num = random.randint(1, 20)
  # numを2で割ってあまりが1であれば、それは出力しないで次のループ処理を行う
  if num % 2 == 1:
    continue

  print(f"{i}回数の結果は{num}です")