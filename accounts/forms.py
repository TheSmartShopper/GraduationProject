from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import StoreAdminProfile, CustomerProfile

user_type = (
    ('Customer', 'Customer'),
    ('StoreAdmin', 'StoreAdmin'),
)


class SignupForm(UserCreationForm):
    typee = forms.ChoiceField(choices=user_type)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'typee'
        ]


class StoreAdminProfileForm(forms.ModelForm):
    class Meta:
        model = StoreAdminProfile
        fields = '__all__'


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = '__all__'



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
