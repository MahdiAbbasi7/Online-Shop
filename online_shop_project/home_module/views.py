from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView

from site_module.models import SiteSetting, FooterLinkBox, Slider
from product_module.models import Product, ProductCategory
from utiles.converters import group_list


class IndexView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)
        latest_product = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        most_visit = Product.objects.filter(is_active=True, is_delete=False).annotate(
            visit_count=Count('productvisit'))[:1]
        context['latest_product'] = group_list(latest_product)
        context['most_visit_product'] = group_list(most_visit)
        categories = list(ProductCategory.objects.annotate(
            product_count=Count('product_category')
        ).filter(is_active=True, is_delete=False)[:6])
        categories_products = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.product_category.all()[:4])
            }
            categories_products.append(item)
        context['categories_products'] = categories_products
        return context


class AboutUsView(TemplateView):
    template_name = 'home_module/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        var = item.footerlink_set
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_component.html', context)
