import random

# 定義エリア
hands = ["グー", "チョキ", "パー"]
gamecount = 0
wincount = 0
losscount = 0

while gamecount < 3:
    # ○回戦
    gamecount = gamecount + 1
    print(f"{gamecount}回戦目開始します")

    while True:
        # 1から3までの値をランダム
        npc = random.randint(1, 3)

        # 入力と同時にstrからintへの変換
        number_hand = int(input("1: グー, 2: チョキ, 3: パー"))

        # 不正な値入力時
        if number_hand < 1 or number_hand > 3:
            print("1から3までの数字を入力してください")
            continue
        # あいこ
        if number_hand == npc:
            print(f"あなたは{hands[number_hand - 1]}NPCは{hands[npc - 1]}なので、あいこです") # [number_hand - 1]はインデックス番号になる
            continue

        # 勝ち
        if (number_hand == 1 and npc == 2) or (number_hand == 2 and npc == 3) or (number_hand == 3 and npc == 1):
            print(f"あなたは{hands[number_hand - 1]}NPCは{hands[npc - 1]}なので、あなたの勝ちです")
            wincount = wincount + 1
            break
        # 負け
        else:
            print(f"あなたは{hands[number_hand - 1]}NPCは{hands[npc - 1]}なので、あなたの負けです")
            losscount = losscount + 1
            break

print(f"ゲーム終了です。あなたの勝ち点は{wincount}です。負けは{losscount}です")