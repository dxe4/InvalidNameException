from google.appengine.ext import ndb


class DoesNotExist(Exception):
    pass


class Article(ndb.Model):
    title = ndb.StringProperty(indexed=False)
    text = ndb.StringProperty(indexed=False)
    url = ndb.StringProperty(indexed=True)
    created = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_by_url(cls, url):
        ancestor = ndb.Key(cls.__name__, url)
        try:
            article = cls.query(ancestor=ancestor).fetch(1)[0]
        except IndexError:
            raise DoesNotExist

        return article
