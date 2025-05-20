import tkinter
import random

WIDTH = 960
HEIGHT = 720
# ボールの座標
ball_x = int(WIDTH / 2)
ball_y = int(HEIGHT / 5)
# ボールの速さ
ball_vx = 10
ball_vy = 10
# バーの座標
bar_x = int(WIDTH / 2)
bar_y = int(HEIGHT - 80)
# スコア
score = 0
hisco = 1000
# ゲームの状態
scene = "タイトル"

def move(e):
    global bar_x
    # e.xの意味は、マウスのx座標を取得する(この形式でないとエラーが出る)
    # バーのx座標はマウスのx座標とする
    bar_x = e.x

    if bar_x < 50:
        # バーのx座標が50より小さくなったら(左側)50(座標の固定)にする
        bar_x = 50
    # 右の端に行ったら(右側)910(座標の固定)にする
    if bar_x > WIDTH - 50:
        # バーのx座標が右の９１０より大きければ９１０で固定
        bar_x = WIDTH - 50

def click(e):
    # 画面をクリックしたらゲームスタート
    global scene, score, ball_x, ball_y, ball_vx, ball_vy
    if scene == "タイトル":
        # ボールの座標を初期化
        ball_x = int(WIDTH / 2)
        ball_y = int(HEIGHT / 5)
        # ボールの速さを初期化
        #ball_vx = 10
        #ball_vy = 10
        ball_vx = random.randint(10, 30)
        ball_vy = random.randint(10, 30)
        # スコアを初期化
        scene = "ゲーム"
        score = 0
    if scene == "ゲームオーバー":
        # ゲームオーバーの処理
        scene = "タイトル"

# テキスト関数の定義
def text(x, y, txt, siz, col):
    fnt = ("Times New Roman", siz)
    cvs.create_text(x + 1, y + 1, text = txt, font = fnt, fill = "black")
    cvs.create_text(x, y, text = txt, font = fnt, fill = col)

def main():
    global ball_x, ball_y, ball_vx, ball_vy, score, hisco, scene
    # cvs.delete("all")はキャンバスの全てを初期化する。初期化しないと、前のフレームが残ってしまい、描画が重なってしまう。
    cvs.delete("all")
    # キャンバスに画像を描画(サイズとbgには画像のパスを指定している)
    cvs.create_image(WIDTH / 2, HEIGHT / 2, image = bg)
    # ボールの実体(バーの内容と同じ)
    #cvs.create_oval(ball_x - 10 , ball_y - 10, ball_x + 10, ball_y + 10, fill = "red")
    cvs.create_image(ball_x, ball_y, image=img)
    # 各変数に加算や減算を行い。座標にピンを打ち。その４点を結ぶことで四角形を描画する
    cvs.create_rectangle(bar_x - 50, bar_y - 5, bar_x + 50, bar_y + 5, fill = "blue")
    # ヒットチェックの範囲を表示
    cvs.create_rectangle(bar_x - 60, bar_y - 20, bar_x + 60, bar_y, fill = "yellow")
    # テキスト関数の呼び出し
    text(200, 30, "SCORE " + str(score), 28, "cyan")
    text(WIDTH - 200, 30, "HIGH SCORE " + str(hisco), 28, "gold")

    if scene == "タイトル":
        # タイトル画面の処理
        text(WIDTH / 2, HEIGHT / 2, "スカッシュゲーム", 60, "green")
        text(WIDTH / 2, HEIGHT / 3 * 2, "CLICK TO START", 30, "lime")

    if scene == "ゲーム":
        # ボールの移動するロジック
        ball_x = ball_x + ball_vx
        ball_y = ball_y + ball_vy
        # ボールが画面の左右の端（10ピクセル以内）で跳ね返ります
        if ball_x < 10 or WIDTH - 10 < ball_x: 
            # 符号の反転させて代入(+なら-、-なら+)
            ball_vx = -ball_vx
        if ball_y < 10:
            ball_vy = -ball_vy
        # 下に落ちたらゲームオーバー
        if ball_y > HEIGHT:
            scene = "ゲームオーバー"

        # バーに当たったら跳ね返るロジック(ヒットチェック)
        dx = ball_x - bar_x
        dy = ball_y - bar_y

        # バーの長さが左60、右60
        # -20はバーの上側座標y座標だから。逆に-20より大きい場合は、バーの下側にあたっているためすり抜ける
        if -60 < dx and dx < 60 and -20 < dy and dy < 0:
            #ball_vy = -10
            ball_vy = random.randint(-15, -1)
            # スコアの加算処理
            score = score + 100
            if hisco < score:
                hisco = score
        
    # ゲームオーバーの処理
    if scene == "ゲームオーバー":
        text(WIDTH / 2, HEIGHT / 2, "GAME OVER", 40, "red")
    # 引数が333ミリ秒で、1秒間に30回main関数を呼び出す。これは1000 % 33 = 30FPS
    # 16にすると60FPSになる
    root.after(33, main)

root = tkinter.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("東堂葵のスカッシュゲーム")
root.resizable(False, False)
cvs = tkinter.Canvas(width = WIDTH, height = HEIGHT)
cvs.pack()
bg = tkinter.PhotoImage(file = "img/bg2.png")
img = tkinter.PhotoImage(file = "img/mouse_point.png")
root.bind("<Motion>", move)
root.bind("<Button>", click)
main()
root.mainloop()