class ContentService:
    def __init__(self, article_factory, repository):
        self.article_factory = article_factory
        self.repository = repository

    def process(self, html):
        article = self.article_factory.create(html)
        yield self.repository.put(article)

