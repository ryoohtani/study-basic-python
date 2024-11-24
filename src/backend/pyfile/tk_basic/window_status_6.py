import tkinter

root = tkinter.Tk()
root.title("ライトニングリターンズ")

window_x = 1080
window_y = 720
cvs = tkinter.Canvas(width = window_x, height = window_y)

img = tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/test_img.png")

cvs.create_image(window_x, window_y, image = img)

cvs.create_rectangle(540, 60, 900, 580, fill = "black", outline = "white", width = 3)

ability = ["H.P", "攻撃力", "魔力", "防御力", "素早さ"]
value = [10000, 2000, 2000, 1200, 1800]

for i in range(5):
    Y = 120 + 80 * i
    cvs.create_text(660, Y, text = ability[i], font = ("TakaoGothic", 20), fill = "white")
    cvs.create_text(800, Y, text = value[i], font = ("TakaoGothic", 24), fill = "white")

cvs.pack()
root.mainloop()


# 課題
# こちらのコードだと描画すると、あまり良くないguiになっている
# なぜ良くないか考えて修正してみる
# その前に、現状のコードをトレース