"""Custom Allauth adapter."""
from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    """Custom Account Adapter."""

    def is_open_for_signup(self, request):
        """Check if signups are open."""
        return True

    def get_login_redirect_url(self, request):
        """get login redirect url."""
        return "/"
