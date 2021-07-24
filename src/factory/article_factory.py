from src.models.article import Article

class ArticleFactory:
    def __init__(self, parser):
        self.parser = parser

    def create(self, html):
        metadata = self.parser.find_metadata(html)
        if not metadata: 
            return 
        url = metadata.get_url()
        content = self.parser.find_content(html)
        return Article(url, metadata, content)
