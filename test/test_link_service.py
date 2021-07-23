import unittest

from src.link_service import LinkService

from test.mocks.mock_parser import MockParser
from test.mocks.mock_repository import MockRepository

MOCK_PARSER = MockParser()
MOCK_REPOSITORY = MockRepository()

LINKS = ['1','2','3']

subject = LinkService(MOCK_PARSER, MOCK_REPOSITORY)

class TestLinkService(unittest.TestCase):
    def test_process(self):
       MOCK_PARSER.when_find_unique_links_then_return(LINKS)
       self.assertEqual(3, subject.process('html'))

if __name__ == '__main__':
    unittest.main()
