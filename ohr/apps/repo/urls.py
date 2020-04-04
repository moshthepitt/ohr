"""repo app URL Configuration."""
from django.urls import path

from ohr.apps.repo.views import (
    CategoryCRUD,
    DocumentCreateView,
    DocumentCRUD,
    DocumentListView,
)

# pylint: disable=invalid-name

app_name = "repo"

views = [
    path("documents", DocumentListView.as_view(), name="search"),
    path("create", DocumentCreateView.as_view(), name="create"),
]

urlpatterns = views + DocumentCRUD().url_patterns() + CategoryCRUD().url_patterns()
