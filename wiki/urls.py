from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.page_list, name="page_list"),
    path("<str:namespace>/<slug:slug>/", views.page_detail, name="page_detail"),
]
