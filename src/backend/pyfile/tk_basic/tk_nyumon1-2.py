# 演習問題: YESとNOのクイズ問題を作成しなさい
import tkinter
from tkinter import messagebox
import math

quiz = [{'question': 'TCP/IPはインターネット通信の基本的なプロトコルである', 'answer': True},
        {'question': 'Javaはオブジェクト指向ではあるが、多重継承をサポートしている', 'answer': False},
        {'question': 'Linuxは無料で利用可能なオープンソースのオペレーティングシステムである', 'answer': True},
        {'question': 'HTTPSはHTTPより速いデータ転送速度をもつ', 'answer': False}
        ]

root = tkinter.Tk()
root.withdraw()

score: int = 0  # スコアの初期化

for index, qa in enumerate(quiz):
    question = qa['question']
    answer = qa['answer']
    user_answer = messagebox.askyesno(f'クイズ 第{index + 1}問', question)

    if user_answer == answer:
        messagebox.showinfo('回答', 'お見事！正解です。')
        score = score + 1
    else:
        messagebox.showinfo('回答','残念！不正解です。')

ritu = math.floor(score / len(quiz) * 100)

messagebox.showinfo('結果', f'お疲れ様でした。{score}問正解。正解率は{ritu}%です。')

root.destroy()
root.mainloop()