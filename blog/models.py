from google.appengine.ext import ndb


class DoesNotExist(Exception):
    pass


class Article(ndb.Model):
    title = ndb.StringProperty(indexed=False)
    text = ndb.StringProperty(indexed=False)
    url = ndb.StringProperty(indexed=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    deleted = ndb.BooleanProperty()

    @classmethod
    def get_by_url(cls, url):
        '''
        Get article by url if exists
        Raises: DoesNotExist Exception
        '''
        ancestor = ndb.Key(cls.__name__, url)
        try:
            article = cls.query(ancestor=ancestor).fetch(1)[0]
        except IndexError:
            raise DoesNotExist

        return article

    @classmethod
    def get_recent(cls, limit=5):
        '''
        Get the last n posted articles
        Raises: DoesNotExist Exception
        '''
        q = cls.query()
        q = q.filter(cls.deleted != True)
        q.order(-cls.created)
        result = q.fetch(limit)

        if not result:
            raise DoesNotExist

        return result
