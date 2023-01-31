from django.contrib.auth.forms import UserChangeForm

from funny.forms_mixins import StyleFormMixin
from users.models import User


class CustomEditUserForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar',)

