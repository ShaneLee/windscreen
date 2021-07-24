from json import JSONEncoder

class Article:
    def __init__(self, url, metadata, content):
        self.url = url
        self.metadata = metadata
        self.content = content

    def get_url(self):
        return self.url

    def get_metadata(self):
        return self.metadata

    def get_content(self):
        return self.content

class ArticleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
