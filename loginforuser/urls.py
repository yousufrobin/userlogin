from django.contrib import admin
from django.urls import path, include
from loginforuser import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.userlogin, name="userlogin"),
    path("logout", views.userlogout, name="userlogout"),
    path("register", views.register, name="register"),
    path("post/<str:variable>", views.post, name="post"),
    path("dynamic", views.dynamic, name="dynamic"),
]
