from django.shortcuts import render #←HTMLをレンダリングをするためのrender関数をimport
from django.views import View #←原型となるViewクラスをimport

#DjangoのViewクラスを継承し、ビュークラスを作る。
class BbsView(View):

    #getメソッドのリクエストがあれば下記を実行
    def get(self, request, *args, **kwargs):

        #処理内容はtemplates/bbs/index.htmlのレンダリングをする。
        return render(request,"bbs/index.html")

#urls.pyから呼び出せるよう、ビュークラスの.as_view()メソッドを実行し、indexに格納する。
index   = BbsView.as_view()
