from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(label='age')
    class Meta:
        model = CustomUser
        fields = ("username", "email" , "age")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email" , "age")