from django.apps import AppConfig


class AdminModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_module'
    verbose_name = 'ماژول سبد خرید'
