class MockScraper:
    def __init__(self):
        self.get_return = None

    def scrape(self, url):
        return self.get_return

    def when_get_then_return(self, val):
        self.get_return = val
