from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from site_module.models import SiteBanner
from .models import Product, ProductCategory, ProductBrand, ProductVisit, ProductGallery
from utiles.http_services import get_client_ip
from utiles.converters import group_list


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['site_banner'] = SiteBanner.objects.filter(is_active=True,
                                                           position__iexact=SiteBanner.SiteBannerPositions.product_list)

        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')

        if start_price is not None:
            query = query.filter(price__gte=start_price)
        if start_price is not None:
            query = query.filter(price__lte=end_price)
        if brand_name is not None:
            query = query.filter(category__url_title__iexact=brand_name)
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query
    #
    # def get_queryset(self):
    #     base_query = super(ProductListView, self).get_queryset()
    #     data = base_query.filter(is_active=True)
    #     return data


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object  # mahsoli k vakeshi shode.
        request = self.request
        favorite_product_id = request.session.get("product_favorite")
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        context['site_banner'] = SiteBanner.objects.filter(is_active=True,
                                                           position__iexact=SiteBanner.SiteBannerPositions.product_detail)
        context['product_galleries'] = group_list(
            list(ProductGallery.objects.filter(product_id=loaded_product.id).all()), 3)
        context['related_products'] = group_list(list(Product.objects.filter(brand_id=loaded_product.brand_id).exclude(pk=loaded_product.id).all()[:12]),3)
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()
        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, id=user_id, product_id=loaded_product.id)
            new_visit.save()
        return context


class AddProductFavorite(View):

    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['product_favorite'] = product.id
        return redirect(product.get_absolute_url())


def product_categories_components(request: HttpRequest):
    products_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': products_categories
    }
    return render(request, 'product_module/components/product_categories_components.html', context)


def product_brands_components(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)
    context = {
        'product_brands': product_brands
    }
    return render(request, 'product_module/components/product_brands_components.html', context)
