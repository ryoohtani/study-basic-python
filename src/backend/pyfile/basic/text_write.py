from pass_env import score_path1

s = '初めてのファイルの書き込み\n'
#s = '2回目のファイルの書き込み\n'
#s = '3回目のファイルの書き込み\n'

# ファイルの内容を上書きする場合は w を使う
# ファイルの内容を追加する場合は a を使う
with open(score_path1, 'a', encoding='utf-8') as f:
    f.write(s)