import tkinter

root = tkinter.Tk()

window_x = 1080
window_y = 720

root.geometry(f"{window_x}x{window_y}")
root.title("ライトニングリターンズ")

cvs = tkinter.Canvas(width = window_x, height = window_y)

img = tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/test_img.png")

img_x = window_x / 2
img_y = window_y / 2 

cvs.create_image(img_x, img_y, image = img)

cvs.create_rectangle(50, 60, 350, 580, fill = "black", outline = "white", width = 3)

ability = ["H.P", "攻撃力", "魔力", "防御力", "素早さ"]
value = [10000, 2000, 2000, 1200, 1800]

for i in range(5):
    Y = 120 + 80 * i
    cvs.create_text(100, Y, text = ability[i], font = ("TakaoGothic", 20), fill = "white")
    cvs.create_text(200, Y, text = value[i], font = ("TakaoGothic", 24), fill = "white")

cvs.pack()
root.mainloop()