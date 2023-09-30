from django.views import View
from django.urls import reverse
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from account_module.models import User
from order_module.models import Order, DetailOrder
from .forms import EditProfileForm, ChangePasswordForm


@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel.html'


@method_decorator(login_required, name='dispatch')
class ChangePasswordPage(View):
    def get(self, request):
        context = {
            'form': ChangePasswordForm()
        }
        return render(request, 'user_panel_module/change_password.html', context)

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('password', "کلمه عبور فعلی اشتباه است.")
        context = {
            'form': form
        }
        return render(request, 'user_panel_module/change_password.html', context)


@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_forms = EditProfileForm(instance=current_user)
        context = {
            'form': edit_forms,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_forms = EditProfileForm(request.POST, request.FILES, instance=current_user)
        if edit_forms.is_valid():
            edit_forms.save(commit=True)
        context = {
            'form': edit_forms
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


@login_required
def user_panel_menu_components(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_components.html')


@login_required
def user_basket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('detailorder_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_price = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_price
    }
    return render(request, 'user_panel_module/user_basket.html', context)


@login_required
def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })

    delete_count, deleted_dict = Order.objects.filter(id=detail_id, order__is_paid=False,
                                                      order__user_id=request.user.id).detail()

    if delete_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    current_order, created = Order.objects.prefetch_related('detailorder_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', {
            'order': current_order,
            'sum': total_amount
        })
    })


@login_required
def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })

    order_detail = DetailOrder.objects.filter(id=detail_id, order__user_id=request.user.id,
                                              order__is_paid=False).first()

    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid'
        })

    current_order, created = Order.objects.prefetch_related('detailorder_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })
