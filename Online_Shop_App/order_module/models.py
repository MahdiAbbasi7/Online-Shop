from django.db import models

# Create your models here.
from account_module.models import User
from product_module.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='پرداخت شده/ نشده')
    payment_day = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return str(self.user)

    def calculate_count(self):
        total_amount = 0
        # if self.is_paid:
        #     for order_detail in self.orderdetail_set.all():
        #         total_amount += order_detail.final_price * order_detail.count
        # else :
        for order_detail in self.orderdetail_set.all():
            total_amount += order_detail.product.price * order_detail.count
        return total_amount

    class Meta:
        verbose_name = 'سبد خرید کاربران '
        verbose_name_plural = 'سبدهای خرید کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تک محصول')
    count = models.IntegerField(verbose_name='تعداد ')

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'لیست های جزییات محصولات'


