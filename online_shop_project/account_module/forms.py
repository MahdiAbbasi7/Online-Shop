from django import forms
from django.core import validators


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(),
        validators=
        [
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(),
        validators=
        [
            validators.MaxLengthValidator(100)
        ]
    )
