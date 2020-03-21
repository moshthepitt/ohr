"""repo app URL Configuration."""
from django.urls import path

from ohr.apps.repo.views import CategoryCRUD, DocumentCRUD, DocumentListView

# pylint: disable=invalid-name

app_name = "repo"

views = [path("documents", DocumentListView.as_view(), name="search")]

urlpatterns = views + DocumentCRUD().url_patterns() + CategoryCRUD().url_patterns()
