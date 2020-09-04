from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video.html', views.video, name='video'),
    path('photography.html', views.photography, name='photography'),
    path('signup.html', views.signup, name='signup'),
    path('signin.html', views.signin, name='signin'),
    path('join.html', views.join, name='join'),
    path('signupdone.html', views.signupdone, name='signupdone'),
    path('board.html', views.board, name='board'),
    path('contents.html', views.contents, name='contents'),
    path('mypage.html', views.mypage, name='mypage'),
]