import unittest

from src.scraper import Scraper

from test.provider.requests_test_provider import RequestsProvider
from test.mocks.mock_requests_response import MockRequestsResponse

URL = 'https://www.ft.com/content/136930dc-16cb-4acc-bdee-09833697244b'

REQUESTS_PROVIDER = RequestsProvider()

class TestScraper(unittest.TestCase):
    def test_scrape(self):
       mock_requests = REQUESTS_PROVIDER.get()         

       expected = 'hello world'
       mock_requests_response = MockRequestsResponse(expected)

       mock_requests.when_get_then_return(mock_requests_response)

       subject = Scraper(REQUESTS_PROVIDER)
       self.assertEqual(expected, subject.scrape(URL))

if __name__ == '__main__':
    unittest.main()

