"""Models module for users app."""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from vega_admin.mixins import TimeStampedModel

USER = settings.AUTH_USER_MODEL


class UserProfile(TimeStampedModel):
    """Model used to store more information on users."""

    user = models.OneToOneField(USER, verbose_name=_("User"), on_delete=models.CASCADE)

    class Meta:
        """Class Meta."""

        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ["user__first_name", "user__last_name", "user__email"]

    def get_name(self):
        """Get pretty name for this user profile."""
        if self.user.get_full_name():
            return self.user.get_full_name()
        if self.user.email:
            return self.user.email
        return self.user.username

    def __str__(self):
        return f"{self.get_name()}'s profile"
