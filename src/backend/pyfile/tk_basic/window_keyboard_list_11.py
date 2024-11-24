import tkinter

FNT = ("Time New Roman", 60)
COLOR_ENTRY = "purple"
COLOR = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
COLOR_ERROR = "white"

def pkey(e):
    # keysymで押されたキーの値を取得できる
    k = e.keysym
    print(type(k))

    if "1" <= k and k <= "7":
        """
        インデックスの取得
        入力番号のスタートは１、インデックス番号は０だからー１する
        keysymの取得した値はstr型だからintにする
        """
        c = int(k)-1
        cvs.delete("all")

        # bgはtkinterの標準オプション
        # fillは文字の色を変更
        cvs["bg"] = COLOR[c]
        cvs.create_text(300, 150, text = COLOR[c], fill = "Black", font = FNT)
    else:
        cvs.delete("all")
        cvs["bg"] = COLOR_ERROR
        cvs.create_text(300, 150, text = COLOR_ERROR, fill = "red", font = FNT)
        
root = tkinter.Tk()

window_x = 600
window_y = 300
root.geometry(f"{window_x}x{window_y}")

root.title("１〜７までのキーの結果を出力するプログラム")

root.resizable(False, False)

cvs = tkinter.Canvas(width = window_x, height = window_y)

# 初期化画面
cvs.delete("all")
cvs["bg"] = COLOR_ENTRY
cvs.create_text(300, 150, text = COLOR_ENTRY, fill = "white", font = FNT)

root.bind("<Key>", pkey)

cvs.pack()

root.mainloop()