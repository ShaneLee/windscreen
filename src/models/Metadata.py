from json import JSONEncoder

class Metadata:
    def __init__(self, url, headline, standfirst, date_published, author, category):
        self.url = url
        self.headline = headline
        self.standfirst = standfirst
        self.date_published = date_published
        self.author = author
        self.category = category
    
    def get_url(self):
        return self.url
    
    def get_headline(self):
        return self.headline

    def get_standfirst(self):
        return self.standfirst

    def get_date_published(self):
        return self.date_published

    def get_author(self):
        return self.author

    def get_category(self):
        return self.category

class MetadataEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
