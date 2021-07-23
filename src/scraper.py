class Scraper:
    def __init__(self, requests):
        self.requests = requests.get()
    
    def scrape(self, url):
        return self.requests.get(url).content
