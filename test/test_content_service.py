import unittest

from src.content_service import ContentService

from test.mocks.mock_article_factory import MockArticleFactory
from test.mocks.mock_repository import MockRepository

MOCK_FACTORY = MockArticleFactory()
MOCK_REPOSITORY = MockRepository()

subject = ContentService(MOCK_FACTORY, MOCK_REPOSITORY)

VAL = 'val'

class TestContentService(unittest.TestCase):
    def test_process(self):
       MOCK_FACTORY.when_create_then_return(VAL)
       self.assertEqual(VAL, subject.process(VAL).__next__())

if __name__ == '__main__':
    unittest.main()
