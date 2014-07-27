from django.conf.urls import patterns, include

urlpatterns = patterns(
    '',
    (r'^appengine_sessions/', include('appengine_sessions.urls')),
    (r'', include('core.urls')),
    (r'', include('blog.urls', namespace='blog', app_name='blog')),
)
