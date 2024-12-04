import tkinter

# 赤い矩形の中心座標
x1 = 200
y1 = 200
# 矩形の横と縦のサイズ
w1 = 80
h1 = 120

# 青い矩形の中心座標
x2 = 400
y2 = 300
# 矩形の横と縦のサイズ
w2 = 240
h2 = 120

# マウスカーソルの関数
def move(e):
    global x1, y1

    # マウスポインタの座標の取得
    x1 = e.x
    y1 = e.y
    col = "red"

    # abs関数は
    """
    abs関数はPythonの組み込み関数で絶対値を求める関数
    絶対値とは、ー５は５になる。０は０になる
    つまり、符号の内容を除いた数字が絶対値になる

    接触判定
    """
    if abs(x1 - x2) <= (w1 + w2) / 2 and abs(y1 - y2) <= (h1 + h2) / 2:
        col = "pink"

    cvs.delete("RED_RECT") 
    """
    マウスの動きに合わせて四角形の作成
    x1 - w1 / 2 と y1 - h1 / 2 で左上の角
    x1 + w1 / 2 と y1 + h1 / 2 で右下の角
    wが矩形の幅
    yが矩形の縦
    """
    cvs.create_rectangle(x1 - w1 / 2, y1 - h1 / 2, x1 + w1 / 2, y1 + h1 / 2, fill = col, outline = "white", tag = "RED_RECT")
        
root = tkinter.Tk()

window_x = 800
window_y = 600
root.geometry(f"{window_x}x{window_y}")

root.title("短形によるヒットチェック")

root.resizable(False, False)

cvs = tkinter.Canvas(width = window_x, height = window_y, bg = "black")

# Motionという記載だからマウスが動くとmove関数が呼ばれる
root.bind("<Motion>", move)

cvs.pack()

# 赤い四角形の初期化
cvs.create_rectangle(x1 - w1 / 2, y1 - h1 / 2, x1 + w1 / 2, y1 + h1 / 2, fill = "red", outline = "white", tag = "RED_RECT")
# 青い四角形の初期化
cvs.create_rectangle(x2 - w2 / 2, y2 - h2 / 2, x2 + w2 / 2, y2 + h2 / 2, fill = "blue", outline = "white")

root.mainloop()