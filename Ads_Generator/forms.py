from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Repeat Password')

    class Meta:
        model = User
        fields = ['username']


    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError('Passwords are not the same.')

        return data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)
