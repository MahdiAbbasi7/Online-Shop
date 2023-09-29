from django.db import models
from django.urls import reverse

from account_module.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان url')
    is_active = models.BooleanField(verbose_name="فعال / غیر فعال")
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده')

    def __str__(self):
        return f'({self.title}-{self.url_title})'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=200, verbose_name="نام برند", db_index=True)
    url_title = models.CharField(max_length=200, verbose_name='نام در آدرس')
    is_active = models.BooleanField(verbose_name="فعال / غیر فعال")

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام')
    category = models.ManyToManyField(ProductCategory, related_name='product_category', verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products', verbose_name='عکس محصولات ')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name="برند", null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=360, null=True, db_index=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True, )
    is_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")
    is_delete = models.BooleanField(verbose_name='حذف شده / حذف نشده')
    slug = models.SlugField(max_length=200, unique=True, default='', null=False, db_index=True, blank=True,
                            verbose_name='عنوان در url')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"


class ProductTag(models.Model):
    caption = models.CharField(max_length=200, db_index=True, verbose_name='عنوان')
    product_tag = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ محصول ها'

    def __str__(self):
        return self.caption


class ProductVisit(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='کاربری که مشاهده کرده است ')

    def __str__(self):
        return f'{self.product.title} / {self.ip} '

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='عکس محصول')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = '  تصاویر گالری'
        verbose_name_plural = 'تصاویرهای گالری'
