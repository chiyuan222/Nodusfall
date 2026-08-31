from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("worldview/", views.worldview, name="worldview"),
    path("new/", views.page_create, name="page_create"),
    path(
        "<str:namespace>/<slug:slug>/edit/",
        views.page_edit,
        name="page_edit",
    ),
    path(
        "<str:namespace>/<slug:slug>/history/",
        views.page_history,
        name="page_history",
    ),
    path(
        "<str:namespace>/<slug:slug>/revision/<int:revision_id>/",
        views.page_revision_detail,
        name="page_revision_detail",
    ),
    path(
        "<str:namespace>/<slug:slug>/revision/<int:revision_id>/revert/",
        views.page_revert,
        name="page_revert",
    ),
    path("<str:namespace>/<slug:slug>/", views.page_detail, name="page_detail"),
    path("", views.page_list, name="page_list"),
]
