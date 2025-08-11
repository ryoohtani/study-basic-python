from pass_env import score_path1

score_list: list = []

with open(score_path1, 'r', encoding='utf-8') as f:
    for baff in f:
        score_list.append(baff)

# i = 4

# score_list.append(str(i) + '\n')

score_list = sorted(score_list, reverse=True)

with open(score_path1, 'w', encoding='utf-8') as f:
    for record in score_list[:5]:
        f.write(str(record))


# 注意: sortとsortedの違い
# sortは元のリストを変更しますが、戻り値はNoneです
# sortedは元のリストを変更せず、新しいソートされたリストを返します。