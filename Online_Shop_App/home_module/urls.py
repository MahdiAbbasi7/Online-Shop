from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name="index_page"),
    path('about-us',views.AboutView.as_view(), name="about_us")
    # path('contact-us', views.contact_page),
    # path('site-header', views.site_header_component,)
]