from django.urls import path
from . import views

urlpatterns = [
    path('site-header', views.site_header_component, name='header' ),
    path('site-footer', views.site_footer_component, name='footer')
]
