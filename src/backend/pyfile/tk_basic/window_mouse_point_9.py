import tkinter

"""
起動時のマウスカーソルの位置をあらかじめ決め打ちする
e.xとe.yで現在のマウスカーソルの座標を取得している
ここで、キャンバスにマウスカーソルが当たらないと、円の
移動は発生しない
そのため、mxとmyの初期値は0でいいと思ったのだが、0にすることで
円が勝手にマウスカーソルのx軸とy軸に移動してしまう
そのため初期値に400と300(画面中央)にすることで整合性が取れる
""" 
mx = 400
my = 300
# マウスカーソルの座標を代入するための役割
def move(e: int):
    global mx, my
    mx = e.x
    my = e.y

# x座標
cx = 400
# y座標
cy = 300
# 円の半径
cr = 50
def main():
    global cx, cy
    if cy > my:
       cy = cy - 5
    
    if cy < my:
        cy = cy + 5

    if cx > mx:
        cx = cx - 5
    
    if cx < mx:
        cx = cx + 5
    
    cvs.delete("all")


    """
    円を作成する(デザイン)
    create_ovalとは、円（楕円）の外接矩形のこと。外接矩形とは、マフィンを作る時型に生地を流し込む
    その型の役割をしていて、その型に収まるように円が中に流し込まれるイメージ

    (cx-cr,  cy-cr)  は左上の角の座標
    (左に移動 上に移動) = 左上の座標が決まる
    例 100 - 50 = 50ここが左上の座標

    (cx+cr, cy+cr)   は右下の角の座標
    (右に移動 下に移動) = 右下の座標が決まる
    例 100 + 50 = 150ここが右下の座標
    """
    # 東堂葵が追いかけてくる
    #cvs.create_image(cx, cy, image = img1)
    cvs.create_image(cx, cy, image = img2)
    # ただの円が追いかけてくる
    #cvs.create_oval(cx-cr, cy-cr, cx+cr, cy+cr, fill = "blue", outline = "cyan")

    # after文は指定した時間に関数を実行するメソッド
    # 50ミリ秒(0.05秒)ごとにmain関数を繰り返し処理を行う
    root.after(50, main)


root = tkinter.Tk()

window_x = 800
window_y = 600
root.geometry(f"{window_x}x{window_y}")

root.title("マウスカーソルを追いかける東堂葵")

# ウィンドウサイズの固定 Falseはウィンドウの固定、trueは可変
root.resizable(False, False)

# マウスカーソルが動いたら、move関数を呼び出す処理
root.bind("<Motion>", move)

cvs = tkinter.Canvas(width = window_x, height = window_y, bg = "black")
# 画像データ情報
#img1 = tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/mouse_point.png")
#img1 = tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/test_imgs.png")
img2 = tkinter.PhotoImage(file = "/src/backend/pyfile/tk_basic/img/photo1.png")
# キャンバスをウィンドウに被せる
cvs.pack()

main()

# 実行
root.mainloop()