from django import forms
from django.contrib.auth.forms import get_user_model, UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm) :
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm) :
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
