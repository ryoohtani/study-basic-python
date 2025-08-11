# ポップアップダイアログの開発練習
import tkinter
# tkinterモジュールのmessageboxモジュールをインポート
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

# メッセージボックス
result = messagebox.showinfo('ポップアップダイアログ', 'こんにちは質問ダイアログです')

# YESとNOのポップアップダイアログ
result = messagebox.askyesno('質問', '猫は好きですか？')
# ポップアップダイアログのボタンを押したらウィンドウを閉じる
if result == True:
    messagebox.showinfo('回答', '猫が好きなんですね！')
    root.destroy()
elif result == False:
    messagebox.showinfo('回答', '猫が好きではないんですね')
    root.destroy()
else:
    root.destroy()
 
root.mainloop()
