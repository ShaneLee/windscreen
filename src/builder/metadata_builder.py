from src.exception.missing_args_exception import MissingArgsException
from src.models.metadata import Metadata

class MetadataBuilder:
    def __init__(self, all_args_required):
        self.all_args_required = all_args_required
        self.url = None
        self.headline = None
        self.standfirst = None
        self.date_published = None
        self.author = None
        self.category = None
        self.url_called = False
        self.headline_called = False
        self.standfirst_called = False
        self.date_published_called = False
        self.author_called = False
        self.category_called = False

    def with_url(self, url):
        self.url_called = True
        self.url = url
        return self
    
    def with_headline(self, headline):
        self.headline_called = True
        self.headline = headline
        return self

    def with_standfirst(self, standfirst):
        self.standfirst_called = True
        self.standfirst = standfirst
        return self

    def with_date_published(self, date_published):
        self.date_published_called = True
        self.date_published = date_published
        return self

    def with_author(self, author):
        self.author_called = True
        self.author = author
        return self

    def with_category(self, category):
        self.category_called = True
        self.category = category
        return self

    def build(self):
        if (self.all_args_required):
            return self._build_all_args() 
        return self._build()

    def _build_all_args(self):
        if (self._all_called()):
            return self._build()
        raise MissingArgsException(self._missing_args())

    def _build(self):
        return Metadata(
            self.url,
            self.headline,
            self.standfirst,
            self.date_published,
            self.author,
            self.category)

    def _missing_args(self):
        return '''url: {0} \nheadline: {1} \nstandfirst: {2} \ndate_published: {3} \nauthor: {4} \ncategory: {5} \n
                '''.format(
                    self._missing(self.url_called),
                    self._missing(self.headline_called),
                    self._missing(self.standfirst_called),
                    self._missing(self.date_published_called),
                    self._missing(self.author),
                    self._missing(self.category_called))
                    

    def _missing(self, val):
        return 'called' if val else 'missing'

    def _all_called(self):
        return self.url_called and self.headline_called and self.standfirst_called and self.date_published_called and self.author_called and self.category_called
