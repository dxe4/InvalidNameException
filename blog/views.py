from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .forms import ArticleForm
from .models import Article


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

create_article = CreatArticle.as_view()
