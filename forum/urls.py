from django.urls import path

from . import views

app_name = "forum"

urlpatterns = [
    path("", views.forum_home, name="forum_home"),
    path("<slug:slug>/", views.board_detail, name="board_detail"),
]
