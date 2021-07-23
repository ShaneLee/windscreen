class LinkService:
    def __init__(self, parser, repository):
        self.parser = parser
        self.repository = repository

    def process(self, html):
        links = list(
            map(self._translate, self.parser.find_unique_article_links(html)))
        print('retrieved ', len(links), ' links')
        return self.repository.put_all(links)

    def _translate(self, link):
        return link.replace('www', 'amp')

