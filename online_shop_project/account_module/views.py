from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from account_module.forms import LoginForm
from .models import User
from django.http import HttpRequest, Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'loginform': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm()
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('index_page'))
                    else:
                        login_form.add_error('email', " کاربری با مشخصات شما یافت نشد")
            else:
                login_form.add_error('email', " کاربری با مشخصات شما یافت نشد")
        context={
            'register_form':login_form
        }
        return render(request, 'account_module/register.html', context)

