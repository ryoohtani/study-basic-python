import tkinter

# グローバル変数 => グローバルにすることで数を常に増加させることができる
i = 0

def count():
    global i

    i = i + 1
    
    # キャンバスに書いたものを削除
    # tkinterでリアルタイム処理を行う際は.delete("all")が必須になる
    # 削除しないと、動作が重くなる
    cvs.delete("all")
    cvs.create_text(200, 100, text = i, font = ("System", 80))

    # ここまできたら再度def countまで戻る(繰り返し処理)
    # 1000は1000ミリ秒 = 1秒ごとにということ
    root.after(1000, count)


# tkinterのウィンドウの基本情報
root = tkinter.Tk()

window_x = 400
window_y = 200
root.geometry(f"{window_x}x{window_y}")
root.title("リアルタイム処理")

# キャンバスをウィンドウに被せる基本情報
cvs = tkinter.Canvas(width = window_x, height = window_y, bg = "blue")

# キャンバスをウィンドウに実際に被せる
cvs.pack()

count()
# 実行
root.mainloop()