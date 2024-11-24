import tkinter

FNT = ("Times New Roman", 30)

def pkey(e):
    cvs.delete("all")
    # キーボードのキーごとのコードを取得
    cvs.create_text(200, 50, text = "コード = " + str(e.keycode), font = FNT)
    # 入力したキーボードを表示
    cvs.create_text(200, 150, text = "シンボル = " + e.keysym, font = FNT)

root = tkinter.Tk()

window_x = 400
window_y = 200
root.geometry(f"{window_x}x{window_y}")

root.title("キーボードの値取得プログラム")

root.resizable(False, False)

# キーボード操作を行うとpkey関数実行
root.bind("<Key>", pkey)

cvs = tkinter.Canvas(width = window_x, height = window_y)

cvs.pack()

root.mainloop()