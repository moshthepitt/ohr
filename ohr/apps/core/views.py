"""Core views module."""
from django.views.generic.base import TemplateView

from ohr.apps.repo.models import Document


class HomePageView(TemplateView):
    """View for home page."""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context["documents"] = Document.objects.all()[:4]
        return context
