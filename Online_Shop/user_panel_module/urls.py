from django.urls import path

from user_panel_module import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('edit-profile', views.EditUserProfilePage.as_view(), name='edit_profile_page'),
    path('change-password', views.ChangePasswordPage.as_view(), name='change_password_page'),
    path('user-basket', views.user_basket, name='user_basket_page'),
    path('remove-order-detail', views.remove_order_detail, name='remove-order-detail_page'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_count_ajax'),
]
