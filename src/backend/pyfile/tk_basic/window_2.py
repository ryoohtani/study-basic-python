import tkinter

# tkinterのウィンドウの基本情報
root = tkinter.Tk()
root.geometry("800x400")
root.title("キャンバスに線を引く")

# キャンバスをウィンドウに被せる基本情報
cvs = tkinter.Canvas(width = 800, height = 600, bg = "black")

# キャンバスに線を描く
cvs.create_line(0, 300, 800, 300, fill = "red", width = 5)
cvs.create_line(400, 0, 400, 600, fill = "blue", width = 20)

# 矩形を描く
cvs.create_rectangle(100, 100, 200, 200, fill = "green", width = 0) 

# 楕円
cvs.create_oval(600, 100, 700, 200, fill = "orange", width = 20)

# 多角形
cvs.create_polygon(200, 450, 100, 550, 300, 550, fill = "purple", width = 20)

# 扇形
cvs.create_arc(600, 450, 700, 550, start = 45, extent = 270, fill = "pink", outline = "")

# 文字の表示
cvs.create_text(300, 250, text = "abcd", font = ("Time New Roman", 10), fill = "white")

# キャンバスをウィンドウに実際に被せる
cvs.pack()

# 実行
root.mainloop()