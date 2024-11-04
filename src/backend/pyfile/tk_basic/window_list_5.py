import tkinter

# tkinterのウィンドウの基本情報
root = tkinter.Tk()
window_x = 1400
window_y = 1400
root.geometry(f"{window_x}x{window_y}")
root.title("配列で色を定義")

# キャンバスをウィンドウに被せる基本情報
cvs = tkinter.Canvas(width = window_x, height = window_y, bg = "black")

rainbow = [["red", "yellow", "green", "blue", "indigo", "violet", "orange"],
           ["gold", "limegreen", "lime", "navy", "skyblue", "cyan", "red"],
           ["red", "yellow", "green", "blue", "indigo", "violet", "orange"]]

for y in range(3):
    for x in range(7):
        Y = y * 200
        X = x * 200
        # Xはx軸のスタート座標
        # 0はy軸のスタート座標
        # X + 120はx軸の終了座標
        # window_yはy軸の終了座標
        # ⚫️⚫️⚫️⚫️⚫️ fillを記載することで、描画するものに対してカラーコードや色を指定できる
        cvs.create_oval(X, Y, X + 200 , Y + 200, fill = rainbow[y][x], width = 0)

# キャンバスをウィンドウに実際に被せる
cvs.pack()

# 実行
root.mainloop()