"""Views module for Vega Admin repo app."""
from vega_admin.utils import get_modelform
from vega_admin.views import VegaCreateView, VegaCRUDView, VegaListView

from ohr.apps.repo.models import Category, Document


class DocumentCreateView(VegaCreateView):  # pylint: disable=too-many-ancestors
    """List view for documents."""

    model = Document
    form_class = get_modelform(Document)
    cancel_url = "/"

    def get_initial(self):
        """Get initial values for form."""
        initial = super().get_initial()
        if not initial.get("user"):
            initial["user"] = self.request.user

        return initial

    def get_form_kwargs(self):
        """Add kwargs to the form."""
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        if kwargs.get("vega_extra_kwargs"):
            kwargs["vega_extra_kwargs"]["cancel_url"] = self.cancel_url
        else:
            kwargs["vega_extra_kwargs"] = {"cancel_url": self.cancel_url}
        return kwargs


class DocumentListView(VegaListView):  # pylint: disable=too-many-ancestors
    """List view for documents."""

    model = Document
    search_fields = ["title", "description"]
    template_name = "documents/list.html"


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
