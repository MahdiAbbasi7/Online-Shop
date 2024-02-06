from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from article_module.models import Article, ArticleCat, ArticleComment


class ArticlesListView(ListView):
    model = Article
    paginate_by = 4
    template_name = 'article_module/articel_page.html'

    def get_context_data(self, *args, object_list=None, **kwargs, ):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        catgory_name = self.kwargs.get('catgory')
        if catgory_name is not None:
            query = query.filter(selected_catgory__url_title__iexact=catgory_name)
        return query


class ArticlesDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super(ArticlesDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticlesDetailView, self).get_context_data()
        article: Article = kwargs.get('object')  # kwargs is a dict
        context['comments'] = ArticleComment.objects.filter(article_id=article.id, parent_id=None).order_by(
            'create_date').prefetch_related(
            'article__articlecomment_set')
        return context


def articel_catgories_partial(request: HttpRequest):
    articel_main = ArticleCat.objects.prefetch_related('articlecat_set').filter(is_active=True, parent=None)
    context = {
        'main_catgories': articel_main
    }
    return render(request, 'components/articel_catgories_components.html', context)


def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated :
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        print(article_id, article_comment, parent_id)
        new_comment = ArticleComment(article_id=article_id, text=article_comment, user_id=request.user.id,
                                      parent_id=parent_id)
        new_comment.save()
    return HttpResponse('response')
