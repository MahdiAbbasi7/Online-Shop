from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('', views.AboutUsView.as_view(), name='about_us'),
    path('site-header', views.site_header_component, name='header'),
    path('site-footer', views.site_footer_component, name='footer')
]
