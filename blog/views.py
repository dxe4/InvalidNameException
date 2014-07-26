from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import Http404, HttpResponse
from .forms import ArticleForm
from .models import Article, DoesNotExist


class CreatArticle(View):
    form_class = ArticleForm
    template_name = 'create_article.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        article = Article(**form.cleaned_data)
        article.put()

        return redirect('blog:show_article', article_url=article.url)


class FetchArticleBase(View):

    def get_article_by_url(self, url):
        try:
            return Article.get_by_url(url)
        except DoesNotExist:
            raise Http404('Article with url {} does not exist'.format(url))

    def get(self, request, *args, **kwargs):
        raise NotImplementedError

    def post(self, request, *args, **kwargs):
        return HttpResponse(status_code=405)


class EditArticle(FetchArticleBase):
    form_class = ArticleForm
    template_name = 'edit_article.html'

    def get(self, request, article_url):
        article = self.get_article_by_url(article_url)

    def post(self, request):
        pass


class DeleteArticle(FetchArticleBase):
    form_class = ArticleForm
    template_name = 'delete_article.html'

    def get(self, request, article_url):
        article = self.get_article_by_url(article_url)

    def post(self, request):
        pass


class ShowArticle(FetchArticleBase):

    def get(self, request, article_url):
        article = self.get_article_by_url(article_url)
        context = {'article': article}
        return render(request, 'show_article.html', context)


def recent_articles(request):
    limit = request.GET.get('limit', 3)
    if limit > 30:  # security reasons
        return HttpResponse(status_code=400)

    try:
        articles = Article.get_recent(limit=limit)
    except DoesNotExist:
        raise Http404('No articles in the databse')

    context = {'articles': articles}

    return render(request, 'recent_articles.html', context)


create_article = CreatArticle.as_view()
delete_article = DeleteArticle.as_view()
edit_article = EditArticle.as_view()
show_article = ShowArticle.as_view()
