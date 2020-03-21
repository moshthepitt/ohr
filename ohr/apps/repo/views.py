"""Views module for Vega Admin repo app."""
from django.views.generic.base import TemplateView

from vega_admin.views import VegaCRUDView

from ohr.apps.repo.models import Category, Document


class DocumentCRUD(VegaCRUDView):
    """CRUD view for Documents."""

    model = Document
    # protected_actions = None
    permissions_actions = None
    list_fields = ["id", "title", "category"]


class CategoryCRUD(VegaCRUDView):
    """CRUD view for Categories."""

    model = Category
    # protected_actions = None
    permissions_actions = None
    list_fields = ["id", "name"]


class HomePageView(TemplateView):
    """View for home page."""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context["documents"] = Document.objects.all()[:4]
        context["feature"] = Document.objects.last()
        context["categories"] = Category.objects.all()[:15]
        return context
