from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', null=True, blank=True, verbose_name='تصویر ')
    email_active_code = models.CharField(max_length=100, verbose_name='کد تایید شدن ایمیل',null= True, blank=True)
    about_user = models.TextField(null=True, blank=True, verbose_name="درباره ی شخص")
    address_user = models.TextField(null=True, blank=True, verbose_name='آدرس شخص')
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
