"""Models module for repo app."""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from vega_admin.mixins import TimeStampedModel

from private_storage.fields import PrivateFileField

USER = settings.AUTH_USER_MODEL


class Category(models.Model):
    """Model definition for Category."""

    name = models.TextField(_("Name"), db_index=True, unique=True)
    description = models.TextField(
        _("Description"),
        db_index=False,
        blank=True,
        default="",
        help_text=_("Describe your project."),
    )

    class Meta:
        """Meta definition for Category."""

        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Document(TimeStampedModel, models.Model):
    """Model definition for Document."""

    user = models.ForeignKey(USER, verbose_name=_("User"), on_delete=models.PROTECT)
    title = models.TextField(_("Title"), db_index=True)
    description = models.TextField(
        _("Description"),
        db_index=False,
        blank=True,
        default="",
        help_text=_("Describe your project."),
    )
    category = models.ForeignKey(
        Category, verbose_name=_("Category"), on_delete=models.PROTECT
    )
    file = PrivateFileField(
        _("File"),
        upload_to="projects/",
        help_text=_("Upload project document"),
        content_types=[
            "application/pdf",
            # ms office
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
            "application/vnd.ms-word.document.macroEnabled.12",
            "application/vnd.ms-word.template.macroEnabled.12",
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
            "application/vnd.ms-excel.sheet.macroEnabled.12",
            "application/vnd.ms-excel.template.macroEnabled.12",
            "application/vnd.ms-excel.addin.macroEnabled.12",
            "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
            "application/vnd.ms-powerpoint",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "application/vnd.openxmlformats-officedocument.presentationml.template",
            "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
            "application/vnd.ms-powerpoint.addin.macroEnabled.12",
            "application/vnd.ms-powerpoint.presentation.macroEnabled.12",
            "application/vnd.ms-powerpoint.template.macroEnabled.12",
            "application/vnd.ms-powerpoint.slideshow.macroEnabled.12",
            "application/vnd.oasis.opendocument.text",
            "text/csv",
        ],
        max_file_size=10485760,
    )

    class Meta:
        """Meta definition for Document."""

        verbose_name = _("Document")
        verbose_name_plural = _("Documents")

    def __str__(self):
        """Unicode representation of Document."""
        return self.title
