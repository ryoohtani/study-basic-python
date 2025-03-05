import tkinter

#scene = "タイトル"
window_w = 1000
window_h = 320
hole_x = 0
ham_x = 0

# フォントの定義
FNT = ("System", 40)
# 下記はテストコード
holes = [1, 0, 2, 0, 1]

def main():
    for i in range(5):
        hole_x = 200 * i + 100
        cvs.create_image(hole_x, 160, image = img[holes[i]])
        cvs.create_text(hole_x, 280, text = i + 1, font = FNT, fill = "purple")

    #ham_x = hole_x
    #cvs.create_image(ham_x , 60, image = ham)

root = tkinter.Tk()
cvs = tkinter.Canvas(width = window_w, height = window_h)
cvs.pack()

img = [tkinter.PhotoImage(file = "img/hole.png"),
       tkinter.PhotoImage(file = "img/mole.png"),
       tkinter.PhotoImage(file = "img/hit.png")
       ]
ham = tkinter.PhotoImage(file = "img/hammer.png")

main()
root.mainloop()