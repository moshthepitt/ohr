"""Apps module for users app."""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Users app config class."""

    name = "ohr.apps.users"
    label = "ohr.users"
