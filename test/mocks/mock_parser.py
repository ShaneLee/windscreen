class MockParser:
    def __init__(self):
        self.url =  None
        self.links =  None
        self.content =  None
        self.metadata =  None

    def find_unique_article_links(self, html):
        return self.links

    def when_find_unique_links_then_return(self, links):
        self.links = links

    def find_content(self, html):
        return self.content

    def when_find_content_then_return(self, content):
        self.content = content

    def find_metadata(self, html):
        return self.metadata

    def when_find_metadata_then_return(self, metadata):
        self.metadata = metadata
