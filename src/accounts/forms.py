from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
