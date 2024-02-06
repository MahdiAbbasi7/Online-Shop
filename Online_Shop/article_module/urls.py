from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='article_view'),
    path('cat/<str:catgory>', views.ArticlesListView.as_view(), name='article_cat_by_list'),
    path('<pk>/', views.ArticlesDetailView.as_view(), name='articles_detail'),
    path('add-article-comment', views.add_article_comment, name='add_article_comment')
]
