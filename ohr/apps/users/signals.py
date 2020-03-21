"""Signals module for users app."""
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from ohr.apps.users.models import UserProfile

USER = settings.AUTH_USER_MODEL


@receiver(post_save, sender=USER)
def create_user_profile(  # pylint: disable=bad-continuation
    sender, instance, created, **kwargs
):  # pylint: disable=unused-argument
    """Create user profile object."""
    if created or not instance.userprofile:
        UserProfile.objects.get_or_create(user=instance)
