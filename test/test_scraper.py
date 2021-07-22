import unittest

from src.scraper import Scraper

URL = 'https://www.ft.com/content/136930dc-16cb-4acc-bdee-09833697244b'

class TestScraper(unittest.TestCase):
    def test_scrape(self):
       mock_requests = MockRequests()         

       expected = 'hello world'
       mock_requests_response = MockRequestsResponse(expected)

       mock_requests.when_get_then_return(mock_requests_response)

       subject = Scraper(mock_requests)
       self.assertEqual(expected, subject.scrape(URL))

class MockRequests:
    def __init__(self):
        self.get_return = None

    def get(self, url):
        return self.get_return

    def when_get_then_return(self, val):
        self.get_return = val

class MockRequestsResponse:
    def __init__(self, content):
        self.content = content

    def content(self):
        return self.content

if __name__ == '__main__':
    unittest.main()

