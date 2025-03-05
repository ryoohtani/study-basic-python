from django.shortcuts import render
from django.views.generic import TemplateView, ListView # TemplateViewはviewクラスの一部。画面を表示するためのviewクラス
                                                        # ListViewはデータの一覧を表示するためのviewクラス
from .models import Product


class Topview(TemplateView):
    template_name = 'hello.html' # テンプレートファイルの指定
    # メモ絶対パスのような記載は不要。

class ProductListVeiw(ListView):
    model = Product
    template_name = "product_list.html"