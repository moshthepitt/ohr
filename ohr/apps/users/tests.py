"""Tests for users app."""
from django.test import TestCase

from model_mommy import mommy

from ohr.apps.users.models import UserProfile


class TestUserModels(TestCase):
    """Test class for User models."""

    def test_userprofile_model_creation(self):
        """Test that a UserProfile model is created when a User is created."""
        user = mommy.make("auth.User", username="mosh")
        # assert that we have a userprofile object attached
        self.assertTrue(isinstance(user.userprofile, UserProfile))
        # check the username
        self.assertEqual("mosh", user.userprofile.user.username)
        # check the __str__ method on UserProfile
        self.assertEqual("mosh's profile", user.userprofile.__str__())

    def test_get_name(self):
        """Test that the get_name method on UserProfile works."""
        user = mommy.make("auth.User", username="mosh")
        self.assertEqual("mosh", user.userprofile.get_name())

        user = mommy.make("auth.User", username="mosh2", email="k@j.com")
        self.assertEqual("k@j.com", user.userprofile.get_name())

        user = mommy.make(
            "auth.User", username="mosh3", first_name="Mosh", last_name="Pitt"
        )
        self.assertEqual("Mosh Pitt", user.userprofile.get_name())
