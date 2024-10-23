import sys
import os
import tkinter as tk

# DISPLAY変数を取得
display = sys.argv[1] if len(sys.argv) > 1 else None

# DISPLAY環境変数を設定 ←これの設定がないと、guiの画面を表示できない
if display:
    os.environ['DISPLAY'] = display

# Tkinterの初期化
root = tk.Tk()
Static1 = tk.Label(text=u'test')
Static1.pack()
root.mainloop()