
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
user_type = (
    ('Customer', 'Customer'),
    ('StoreAdmin', 'StoreAdmin'),
)
class SignupForm(UserCreationForm):
    typee= forms.ChoiceField(choices=user_type)
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'typee'
        ]
