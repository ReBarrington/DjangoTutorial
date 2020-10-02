from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # nested configurations. model affected will be User, and fields in the order we want
        model = User
        fields = ['username', 'email', 'password1', 'password2']