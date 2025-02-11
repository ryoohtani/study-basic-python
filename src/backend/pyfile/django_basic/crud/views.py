from django.shortcuts import render
from django.views.generic import TemplateView # TemplateViewはviewクラスの一部。画面を表示するためのviewクラス

class Topview(TemplateView):
    template_name = 'hello.html' # テンプレートファイルの指定
    # メモ絶対パスのような記載は不要。