from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home_module.urls')),
    path('', include('account_module.urls')),
    path('articles/', include('article_module.urls')),
    path('contact-us/', include('contact_module.urls')),
    path('products/', include('product_module.urls')),
    path('user/', include('user_panel_module.urls')),
    path('order/', include('order_module.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
