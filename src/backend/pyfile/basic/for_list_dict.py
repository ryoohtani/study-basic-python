users_table = ["ショーン・オマリー", "メラブ・ドバリシビリ", "コーリー・サンドヘイゲン", "ピョートル・ヤン", "マルロン・ヴェラ", "ヘンリー・セフード"]

users_box = "コーリー・サンドヘイゲン"

for user_name in users_table:
    if user_name == users_box:
        break
    print(user_name)




########## ここから下は辞書型 ##########
player_data = {"name":"ショーン・オマリー", "age":29, "weight":"バンタム"}

"""
.item()とは
 辞書からキーと値をセットで取り出す関数
"""
for key, value in player_data.items():
    print(f"{key}は{value}です")

# valueのみの値を取り出す方法(メソッドには最後にsを忘れず)
for value in player_data.values():
    print(value)




score = {"国語":100, "数学":90,"社会":80,"科学":70,"英語":60}

for key, value in score.items():
    if value < 70:
        continue
    print(f"{key}は{value}です")