from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
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

        return HttpResponseRedirect('')


def show_article(request, article_url):
    try:
        article = Article.get_by_url(article_url)
    except DoesNotExist:
        raise Http404('Article with url {} does not exist'.format(article_url))

    context = {'article': article}
    return render(request, 'show_article.html', context)

create_article = CreatArticle.as_view()
