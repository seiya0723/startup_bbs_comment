from django.urls import path
from . import views

#逆引きするときの名前はbbs
app_name    = "bbs"
urlpatterns = [
    #トップページにアクセスした時、views.pyの中のindexという処理を呼び出す。(indexはIndexView.as_view()なのでその中の処理が実行される。)
    path('', views.index, name="index"),
]
