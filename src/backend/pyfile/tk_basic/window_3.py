import tkinter

# tkinterのウィンドウの基本情報
root = tkinter.Tk()
window_x = 1080
window_y = 720
root.geometry(f"{window_x}x{window_y}")
root.title("キャンバスに画像を表示")

# キャンバスをウィンドウに被せる基本情報
cvs = tkinter.Canvas(width = window_x, height = window_y, bg = "black")

# 画像データを読み込む
img = tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/test_img.png")

# キャンバスに画像の座標の決定と表示
img_x = window_x / 2
img_y = window_y / 2
# 引数のxとyはキャンバスに対して画像をどこの座標に配置するか？ということ
cvs.create_image(img_x, img_y, image = img) #imageはキーワード変数だから基本構文ということになる

# キャンバスをウィンドウに実際に被せる
cvs.pack()

# 実行
root.mainloop()