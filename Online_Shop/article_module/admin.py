from django.contrib import admin
from django.http import HttpRequest

from . import models


# Register your models here.
from .models import Article


class ArticleCatAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'is_active', 'parent']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, form, change, obj)


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['user','parent', 'create_date']


admin.site.register(models.ArticleCat, ArticleCatAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ArticleComment, ArticleCommentAdmin)
