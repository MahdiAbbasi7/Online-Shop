from django.urls import path
from . import views

urlpatterns = [
    # path('', views.contact_us_page, name="contact_us_page"),
    path('', views.ContactUsView.as_view(), name='contact_us_page'),
    path('create-profile/', views.CreateProfileView.as_view(), name='Create_Profile_Page'),
    path('profiles/', views.ProfileListView.as_view(), name='profiles_page'),
]
