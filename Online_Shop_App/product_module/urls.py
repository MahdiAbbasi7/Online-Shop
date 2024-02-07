from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_list, name='product_list'),
    path('', views.ProductListView.as_view(), name='product_list'),
    # path('detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product_categories_list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product_brand_list'),
    path('product-favorite', views.AddProductFavorite.as_view(), name='product-favorite'),
    path('detail/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail')

]
