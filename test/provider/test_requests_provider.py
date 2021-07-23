import unittest

from src.provider.requests_provider import RequestsProvider

class TestRequestsProvider(unittest.TestCase):
    def test_get_requests(self):
       self.assertIsNotNone(RequestsProvider().get())

if __name__ == '__main__':
    unittest.main()
