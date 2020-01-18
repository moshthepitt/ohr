"""repo app URL Configuration."""
from ohr.apps.repo.views import CategoryCRUD, DocumentCRUD

# pylint: disable=invalid-name
urlpatterns = DocumentCRUD().url_patterns() + CategoryCRUD().url_patterns()
