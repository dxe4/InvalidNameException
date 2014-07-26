from django import forms
from google.appengine.ext import ndb


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=150)
    text = forms.CharField(max_length=30000)  # TL;DR

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()

        key = ndb.Key('Article', cleaned_data.get('title'))
        cleaned_data['key'] = key

        return cleaned_data
