from copy import copy
from datetime import datetime
from functools import partial
import unittest
from google.appengine.ext import ndb
from ndbtestcase import AppEngineTestCase
from .models import Article, DoesNotExist
from .forms import ArticleForm


default_article = {
    'title': 'spam eggs',
    'text': 'spam spam spam spam spam',
}


class ArticleTestCase(AppEngineTestCase):

    def __init__(self, *args, **kwargs):
        super(ArticleTestCase, self).__init__(*args, **kwargs)
        self.data = copy(default_article)


class ArticleDBTestCase(ArticleTestCase):

    """Example App Engine testcase"""

    def test_create(self):
        form = ArticleForm(self.data)
        assert form.is_valid()

        article = Article(**form.cleaned_data)
        article.put()
        articles = Article.query().fetch(2)

        assert len(articles) == 1
        article = articles[0]

        # ensure slug works
        assert article.url == 'spam-eggs'
        # ensure auto_now_add works
        assert isinstance(article.created, datetime)

    def test_get_recent(self):
        article = Article(**self.data)
        article.put()

        data = copy(self.data)
        data['title'] = 'foo bar'
        article = Article(**data)
        article.put()

        articles = Article.get_recent()

        assert len(articles) == 2

    def test_get_recent_no_data(self):
        self.assertRaises(DoesNotExist, Article.get_recent)

    def test_get_by_url(self):
        form = ArticleForm(self.data)
        assert form.is_valid()

        article = Article(**form.cleaned_data)
        article.put()

        article = Article.get_by_url('spam-eggs')
        assert article.url == 'spam-eggs'

    def test_get_by_url_exception(self):
        p_get_by_url = partial(Article.get_by_url, 'foo-bar')
        self.assertRaises(DoesNotExist, p_get_by_url)


# from django.test import TestCase
class DjangoTest(object):
    def test_create(self):
        '''
        form invalid -> render create page
        form valid -> redirect to created article
        '''
        pass

    def test_delete(self):
        '''
        ensure obj is deleted in the db and redirect to recent_articles
        '''
        pass

    def test_edit(self):
        '''
        form invalid -> render edit_article
        form valid -> redirect to edited_article
        '''
        pass

    def test_recent_articles(self):
        '''
        get param limit > 30 -> code = 400
        empty db -> 404
        else render recent_articles
        '''
        pass

if __name__ == '__main__':
    unittest.main()
