from pass_env import score_path1

# ファイルの内容を上書きする場合は w を使う
# ファイルの内容を追加する場合は a を使う
with open(score_path1, 'a', encoding='utf-8') as f:
    for i in range(1, 6):
        f.write(str(i) + '\n')