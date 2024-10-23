# :intとは引数の型ヒントのこと(明示的にわかりやすくするため)
def amazon(shohin1, shohin2: int):
    # 送料500円
    souryou = 500
    # 商品の単価と送料の合計金額
    shohin_goukei = shohin1 + shohin2 + souryou
    # 領収書の印刷のイメージ
    print(f"お客様の商品合計金額は{shohin_goukei}円です")

amazon(1200, 30000)