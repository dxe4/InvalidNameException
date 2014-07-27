from django import forms
from django.template.defaultfilters import slugify
from google.appengine.ext import ndb


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=150)
    text = forms.CharField(max_length=30000)  # TL;DR

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()

        # probably this has to go in the model
        url = slugify(cleaned_data['title'])
        key = ndb.Key('Article', url)

        cleaned_data['key'] = key
        cleaned_data['url'] = url

        return cleaned_data
