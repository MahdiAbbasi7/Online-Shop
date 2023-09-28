from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """This class for create a new user."""

    avatar = models.ImageField(upload_to='images/profile', null=True, blank=True, verbose_name='تصویر')
    email_active_code = models.EmailField(max_length=100, verbose_name='کد تایید شدن ایمیل', null=True, blank=True)
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره ی کاربر')
    address_user = models.TextField(null=True, blank=True, verbose_name='آدرس کاربر')

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        return self.email
