import tkinter

# 文字の定義
FNT = ("Time New Roman", 40)

def move(mouse_event: int):
    # キャンバスに書いたものを削除
    # tkinterでリアルタイム処理を行う際は.delete("all")が必須になる
    # 削除しないと、動作が重くなる
    cvs.delete("all")

    s = "({}, {})".format(mouse_event.x, mouse_event.y)
    cvs.create_text(400, 200, text = s, font = FNT)

# tkinterのウィンドウの基本情報
root = tkinter.Tk()
window_x = 800
window_y = 400
root.geometry(f"{window_x}x{window_y}")

root.title("マウスの座標")

# ⚫️イベント発生時、対象の関数呼び出す bind()
root.bind("<Motion>", move)
# キャンバスをウィンドウに被せる基本情報
cvs = tkinter.Canvas(width = window_x, height = window_y)

# キャンバスをウィンドウに実際に被せる
cvs.pack()
# 実行
root.mainloop()