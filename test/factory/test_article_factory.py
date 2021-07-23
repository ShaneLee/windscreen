import unittest

from src.factory.article_factory import ArticleFactory
from src.models.article import Article
from src.models.metadata import Metadata

from test.mocks.mock_parser import MockParser

URL = 'https://www.ft.com/content/136930dc-16cb-4acc-bdee-09833697244b'

CONTENT = 'test'
METADATA = Metadata(URL, None, None, None, None, None)

links = ['1','2','3']

MOCK_PARSER = MockParser()

EXPECTED = Article(URL, METADATA, CONTENT)

class TestArticleFactory(unittest.TestCase):
    def test_create(self):
       MOCK_PARSER.when_find_content_then_return(CONTENT)
       MOCK_PARSER.when_find_metadata_then_return(METADATA)
       subject = ArticleFactory(MOCK_PARSER)
       result = subject.create('html')

       self.assertEqual(URL, result.get_url())
       self.assertEqual(METADATA, result.get_metadata())
       self.assertEqual(CONTENT, result.get_content())

if __name__ == '__main__':
    unittest.main()
