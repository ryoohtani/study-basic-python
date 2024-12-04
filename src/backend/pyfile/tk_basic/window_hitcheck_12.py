import tkinter

# 赤い円
x1 = 200
y1 = 200
# 円の半径
r1 = 60

# 青い円
x2 = 500
y2 = 300
# 円の半径
r2 = 120

# キー操作関数
def pkey(e):
    global x1, y1

    # 下記理屈を理解していない場合は、座標の関係性について理解していないから
    # 座標の学習を確認すること
    if e.keysym == "Up":
        y1 = y1 - 10
    if e.keysym == "Down":
        y1 = y1 + 10
    if e.keysym == "Left":
        x1 = x1 - 10
    if e.keysym == "Right":
        x1 = x1 + 10 

    """
    ** 0.5は平方根
    **の意味は２乗という意味
    ここで平方根の値を算出
    """    
    d = ((x1 - x2)** 2 + (y1 - y2)** 2) ** 0.5

    col = "red"
    # 中間距離であるdより赤い円と青い円の半径の方が大きいか判定
    if d <= r1 + r2:
        # 中間距離が小さくなり、１の円と２の円が接触したらピンク色になる
        col = "pink"

    cvs.delete("RED_CIRCLE")
    cvs.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill = col, outline = "white", tag = "RED_CIRCLE")
        
root = tkinter.Tk()

window_x = 800
window_y = 600
root.geometry(f"{window_x}x{window_y}")

root.title("円によるヒットチェック")

root.resizable(False, False)

cvs = tkinter.Canvas(width = window_x, height = window_y, bg = "black")

root.bind("<Key>", pkey)

cvs.pack()

cvs.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill = "red", outline = "white", tag = "RED_CIRCLE")

cvs.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill = "blue", outline = "white")

root.mainloop()