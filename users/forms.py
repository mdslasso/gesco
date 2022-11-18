from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2", "is_superuser"]
