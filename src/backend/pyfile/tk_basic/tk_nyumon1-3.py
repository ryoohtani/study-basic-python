# 計算アプリ
# 仕様変更として、小数点以下第２までに制限すること
import tkinter
# tkinterモジュールのmessageboxモジュールをインポート
from tkinter import messagebox
import random

# グローバル変数
# UI部品をグローバル変数にしておく
# これにより、関数の中でUI部品を参照できる
Label1: tkinter.Label = None
Entry1: tkinter.Entry = None
root: tkinter.Tk = None

# 計算式用の変数と四則演算式のグローバル変数
left_cal: int = 0
symbol: str = ''
right_cal: int = 0
result: int = 0

def setcal_func():
    global left_cal, right_cal, symbol, result

    symbol_list: list = ['+', '-', '*', '/']
    
    err_flag: bool = True
    while err_flag == True:

        left_cal = random.randint(0, 100)
        right_cal = random.randint(0, 100)
        symbol = random.choice(symbol_list)

        if symbol == '+':
            result = left_cal + right_cal
        elif symbol == '-':
            result = left_cal - right_cal
        elif symbol == '*':
            result = left_cal * right_cal
        elif symbol == '/':
            if right_cal == 0:
                continue
            result = left_cal / right_cal
            err_flag: bool = True
        else:
            messagebox.showerror('エラー', '計算式の設定に失敗しました')
            return None, None, None, None
        
        err_flag: bool = False
    
    if result is not None:
        Label1.config(text=f"問題です。{left_cal} {symbol} {right_cal} はいくつですか？")
    
    if Entry1 is not None:
        Entry1.delete(0, tkinter.END)

def create_window_func(root, left_cal, symbol, right_cal):
    global Label1, Entry1
    window_x: int = 500
    window_y: int = 300
    root.geometry(f"{window_x}x{window_y}")
    root.title("暗算練習")
    root.resizable(False, False)

    Label1 = tkinter.Label(text = f"問題です。{left_cal} {symbol} {right_cal} はいくつですか？")
    Label1.place(x = 150, y = 50) # 描画する

    Entry1 = tkinter.Entry(width = 30)
    Entry1.place(x = 120, y = 100)
    # フォーカスのセット
    Entry1.focus_set()

    frames_1: tkinter.Frame = tkinter.Frame(root) # 前回の回答を表示するためのフレーム
    frames_1.place(x = 150, y = 200, width = window_x, height = 100)

    button1: tkinter.Button = tkinter.Button(text = "OK", command = lambda: show_entry(frames_1))
    button1.place(x = 160, y = 150)

    root.bind("<Return>", lambda event: show_entry(frames_1)) # エンターキーで入力を送信(bindを使う際はeventを引数に取る必要があります)

    """
    lambdaは無名関数
    tkinterはイベント駆動型のプログラミングを採用しているため、ボタンが押されたときに特定の関数を実行するためにlambdaを使用します。
    関数に引数があることで、即時実行されてしまうため、lambdaを使って関数をラップします。
    これにより、ボタンが押されたときにのみ関数が実行されるようになります。
    例えば、command=show_end(root)とすると、show_end関数が即座に実行されてしまいます。
    そのため、lambdaを使って、ボタンが押されたときにshow_end関数を呼び出すようにします。
    具体的には、command=lambda: show_end(root)とすることで、ボタンが押されたときにshow_end関数が実行されるようになります。
    これにより、ボタンが押されたときにのみshow_end関数が実行されるようになります。
    つまり、lambdaは関数を遅延評価するための方法であり、イベント駆動型のプログラミング
    """
    button2: tkinter.Button = tkinter.Button(text = "close", command = lambda: show_end(root))
    button2.place(x = 270, y = 150)

    root.bind("<Escape>", lambda event: show_end(root)) # エスケープキーでアプリを終了する

def show_entry(frames_1: tkinter.Frame):
    global result
    inch_str: str = Entry1.get()

    if inch_str == '' or inch_str is None:
        messagebox.showinfo( '入力確認', '何も入力されませんでした')
        return
    
    try:
        inch_int: float = float(inch_str)
    except ValueError:
        messagebox.showerror('エラー確認', '数値を入力してください')
        return
    
    if inch_int == result:
        messagebox.showinfo('結果', '正解です！')
        Label2 = tkinter.Label(frames_1, text = f"前回答え。{result}", anchor = "center")
        Label2.pack(anchor='w')
    else:
        messagebox.showinfo('結果', f'不正解です。正解は {result} です')
        Label2 = tkinter.Label(frames_1, text = f"前回答え。{result}", anchor = "center")
        Label2.pack(anchor='w')
    
    setcal_func()

def show_end(root):
    result = messagebox.askyesno('入力確認', 'アプリを終了しますか？')

    if result == True:
        root.destroy()
        exit(0)
    else:
        return None

def main():
    global root, left_cal, symbol, right_cal
    root = tkinter.Tk()
    create_window_func(root, left_cal, symbol, right_cal)
    setcal_func()
    root.mainloop() # ここにきてユーザーが実際にアプリを操作できる
    
if __name__ == "__main__":
    main()