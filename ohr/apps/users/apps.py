"""Apps module for users app."""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Users app config class."""

    name = "ohr.apps.users"
    label = "ohr.users"

    def ready(self):
        """Run when ready."""
        # pylint: disable=import-outside-toplevel,unused-import
        from ohr.apps.users import signals  # noqa
