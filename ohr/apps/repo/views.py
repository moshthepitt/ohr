"""Views module for Vega Admin repo app."""
from vega_admin.views import VegaCRUDView

from ohr.apps.repo.models import Category, Document


class DocumentCRUD(VegaCRUDView):
    """CRUD view for Documents."""

    model = Document
    protected_actions = None
    permissions_actions = None
    list_fields = ["id", "title", "category"]


class CategoryCRUD(VegaCRUDView):
    """CRUD view for Categories."""

    model = Category
    protected_actions = None
    permissions_actions = None
    list_fields = ["id", "name"]
