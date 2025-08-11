# テキストエディタをtkinterで作成
import tkinter
from tkinter import filedialog

open_path = ""

def create_window_func(root):
    window_x: int = 680
    window_y: int = 400
    root.geometry(f"{window_x}x{window_y}") 
    root.title("テキストエディタミラー用")
    #root.resizable(False, False)

    # テキストエリアの作成
    text_area: tkinter.Text = tkinter.Text(root, height = 100, width = 190)
    text_area.pack()

    menubar: tkinter.Menu = tkinter.Menu()
    root.config(menu = menubar) # メニューバーのグループの枠組みのこと
    # ファイルメニューの作成
    file_menu: tkinter.Menu = tkinter.Menu(menubar)
    menubar.add_cascade(label = "ファイル", menu = file_menu)
    file_menu.add_command(label = "新規作成", command = lambda: text_area.delete("1.0", tkinter.END))
    file_menu.add_command(label = "開く", command = lambda: open_func(text_area))
    file_menu.add_command(label = "上書き保存", command = lambda: update_func(text_area))
    file_menu.add_command(label = "名前を付けて保存", command = lambda: save_func(text_area))
    file_menu.add_command(label = "閉じる", command = root.quit)

def open_func(text_area: tkinter.Text):
    flopen_path = filedialog.askopenfilename() 

    if not flopen_path or not isinstance(flopen_path, str):
        return
    
    with open(flopen_path, 'r', encoding = "utf-8") as file:
        text_read = file.read()
    
    text_area.delete("1.0", tkinter.END)  # テキストエリアをクリア
    text_area.insert(tkinter.END, text_read)  # テキストエリアに読み込んだ内容を挿入

def update_func(text_area: tkinter.Text):
    global open_path
    if open_path == "":
        open_path = ""
        return
    
    get_text = text_area.get("1.0", tkinter.END)
    with open(open_path, 'w', encoding = "utf-8") as file:
        file.write(get_text)

def save_func(text_area: tkinter.Text):
    global open_path
    # ファイルの保存するときのダイアログを出す
    flsave_path = filedialog.asksaveasfilename() 

    # 左辺はflsave_pathが空なら、右辺はflsave_pathがstr型でなければ
    # tkinterのfiledialog.asksaveasfilenameの戻り値がバージョンによってタプルが入ったりするから(仕様としてはよくないよね)
    if not flsave_path or not isinstance(flsave_path, str): 
        return

    # テキストエリアの内容を取得(第一引数は開始位置、第二引数は終了位置)
    get_text = text_area.get("1.0", tkinter.END) 

    with open(flsave_path, 'w', encoding = "utf-8") as file:
        file.write(get_text)
    
    open_path = flsave_path  # グローバル変数に保存


def main():
    root: tkinter.Tk = tkinter.Tk()
    create_window_func(root)
    root.mainloop()

if __name__ == "__main__":
    main()