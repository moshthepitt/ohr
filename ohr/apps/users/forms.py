"""Forms module for users app."""
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import ugettext as _

from allauth.account.forms import SignupForm as AllauthSignupForm
from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from ohr.apps.core import constants


class SignupForm(  # pylint: disable=bad-continuation
    AllauthSignupForm, forms.ModelForm
):  # pylint: disable=too-many-ancestors
    """Custom registration form."""

    first_name = forms.CharField(label=_(constants.FIRST_NAME), required=True)
    last_name = forms.CharField(label=_(constants.LAST_NAME), required=True)
    board_num = forms.CharField(label=_(constants.BOARD_NUMBER), required=True)

    class Meta:
        """Class Meta options."""

        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def save(self, request=None):
        """Custom save method."""
        user = super().save(request)
        if constants.BOARD_NUM_FIELD in self.cleaned_data:
            user.userprofile.data[constants.BOARD_NUM_FIELD] = self.cleaned_data[
                constants.BOARD_NUM_FIELD
            ]
        user.userprofile.save()
        return user

    def __init__(self, *args, **kwargs):
        """Init method."""
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_action = reverse("account_signup")
        self.helper.form_method = "post"
        self.helper.render_required_fields = True
        self.helper.form_show_labels = True
        self.helper.html5_required = True
        self.helper.form_id = "signup-form"
        self.helper.layout = Layout(
            Field("first_name", placeholder=_(constants.FIRST_NAME)),
            Field("last_name", placeholder=_(constants.LAST_NAME)),
            Field("email", placeholder=_(constants.EMAIL_ADDRESS)),
            Field("board_num", placeholder=_(constants.BOARD_NUMBER)),
            Field("password1", autocomplete="off"),
            Field("password2", autocomplete="off"),
        )
