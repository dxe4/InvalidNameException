from django.conf.urls.defaults import url, patterns


urlpatterns = patterns(
    'blog.views',
    # view
    url(r'^article/(?P<article_url>[\w-]+)/show$',
        'show_article', {}, name='show_article'),
    # moderate
    url(r'^admin/article$', 'create_article',
        {}, name='create_article'),
    url(r'^article/(?P<article_url>[\w-]+)/edit$', 'edit_article',
        {}, name='edit_article'),
    url(r'^article/(?P<article_url>[\w-]+)/delete$', 'delete_article',
        {}, name='delete_article'),
    # aggregate
    url(r'^article/recent$',
        'recent_articles', {}, name='recent_articles'),
)
