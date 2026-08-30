from django.urls import path

from . import views

app_name = "media"

urlpatterns = [
    path("add/", views.media_add, name="media_add"),
    path("", views.media_list, name="media_list"),
    path("<int:pk>/", views.media_detail, name="media_detail"),
]
