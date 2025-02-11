import tkinter

scene = "タイトル"
player_x = 0
player_a = 0
window_x1 = 960
window_y1 = 640
window_x2 = 480
window_y2 = 320
window_t1 = 180
window_t2 = 420

def pkey(e):
    global scene
    if e.keysym == "space":
        scene = "ゲーム"
    if e.keysym == "Return":
        scene = "タイトル"

def main():
    global player_x, player_a, window_x2, window_y2, window_t1, window_t2
    cvs.delete("all")
    cvs.create_image(window_x2, window_y2, image = bg)
    
    if scene == "タイトル":
        cvs.create_image(window_x2, window_y2, image = ilst)
        cvs.create_text(window_x2, window_t1, text = "走る", font = ("System", 100), fill = "lime")
        cvs.create_text(window_x2, window_t2, text = "press [SPACE] key", font = ("System", 40), fill = "cyan")
    
    if scene == "ゲーム":
        player_x = player_x + 40

        if player_x > 960: player_x = 0

        player_a = player_a + 1

        cvs.create_image(player_x, 400, image = main_player[main_player%4])
    
    root.after(100, main)


root = tkinter.Tk()

root.geometry(f"{window_x1}x{window_y1}")

root.title("走るゲーム")

root.resizable(False, False)

cvs = tkinter.Canvas(width = window_x1, height = window_y1)

root.bind("<Key>", pkey)

cvs.pack()

ilst = tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/illust.png")

bg = tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/bg.png")

main_player = [tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/ninja0.png"),
               tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/ninja1.png"),
               tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/ninja2.png"),
               tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/ninja3.png")]

main()

root.mainloop()


# プログラムにはバグがある。その内容をgptを使わないで考えること