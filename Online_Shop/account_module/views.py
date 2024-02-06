from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from account_module.forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from utiles.email_sevice import send_email
from .models import User
from django.http import Http404, HttpRequest
from django.contrib.auth import login, logout


# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'این ایمیل قبلا ثبت نام شده')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(48),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user},
                           'templates/email/active_account.html')
                return redirect(reverse('login_page'))
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(48)
                user.save()
                # todo  show success message to user
                return redirect(reverse('login_page'))
            else:
                # todo show your was activated message to user
                pass
        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
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

        context = {
            'register_form': login_form
        }
        return render(request, 'account_module/register.html', context)


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_password_form = ForgetPasswordForm()
        context = {
            'forget_password_form': forget_password_form
        }
        return render(request, 'account_module/forgat_password.html', context)

    def post(self, request: HttpRequest):
        forget_password_form = ForgetPasswordForm(request.POST)
        if forget_password_form.is_valid():
            user_email = forget_password_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                pass

        context = {
            'forget_password_form': forget_password_form
        }
        return render(request, 'account_module/forgat_password.html', context)


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__exact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))
        reset_password_form = ResetPasswordForm()
        context = {
            'reset_password_form': reset_password_form,
            'user': user
        }
        return render(request, 'account_module/reset_password.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_password_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_password_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))
            user_new_password = reset_password_form.cleaned_data.get('password')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(48)
            user.is_active = True
            user.save()
            return redirect(reverse('index_page'))
        context = {
            'reset_password_form': reset_password_form,
            'user': user
        }
        return render(request, 'account_module/reset_password.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
