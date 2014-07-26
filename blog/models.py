from google.appengine.ext import ndb


class Article(ndb.Model):
    title = ndb.StringProperty(indexed=False)
    text = ndb.StringProperty(indexed=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
