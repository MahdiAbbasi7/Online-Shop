from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account_module.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'about_user', 'address_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'about_user': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 6,
                'id': 'message'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
        }
        labels = {
            'first_name': 'نام ',
            'last_name': ' نام خانوادگی شما',
            'avatar': 'تصویر شما',
            'about_user': 'درباره ی شما',
            'address': 'آدرس شما',
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')
