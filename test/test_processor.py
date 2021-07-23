import unittest

from src.processor import Processor

from test.mocks.mock_content_service import MockContentService
from test.mocks.mock_config import MockConfig
from test.mocks.mock_generator import MockGenerator
from test.mocks.mock_link_service import MockLinkService
from test.mocks.mock_scheduler import MockScheduler
from test.mocks.mock_scraper import MockScraper

URL = 'https://www.ft.com/content/136930dc-16cb-4acc-bdee-09833697244b'

LINKS = ['1','2','3']

MOCK_CONTENT_SERVICE = MockContentService()
MOCK_CONFIG = MockConfig()
MOCK_SCRAPER = MockScraper()
MOCK_SCHEDULER = MockScheduler()
MOCK_LINK_SERVICE = MockLinkService()

class TestProcessor(unittest.TestCase):
    def test_process(self):
        subject = Processor(
            MOCK_CONFIG,            
            MOCK_SCHEDULER, 
            MockGenerator(LINKS),
            MOCK_SCRAPER,
            MOCK_CONTENT_SERVICE,
            MOCK_LINK_SERVICE
        )

        result = []
        MOCK_SCRAPER.when_get_then_return(LINKS[0])
        result.append(list(subject.process())[0])
        MOCK_SCRAPER.when_get_then_return(LINKS[1])
        result.append(list(subject.process())[0])
        MOCK_SCRAPER.when_get_then_return(LINKS[2])
        result.append(list(subject.process())[0])
        self.assertEqual(LINKS, result)

    def test_process_empty_generator(self):
        subject = Processor(
            MOCK_CONFIG,            
            MOCK_SCHEDULER, 
            MockGenerator(LINKS),
            MOCK_SCRAPER,
            MOCK_CONTENT_SERVICE,
            MOCK_LINK_SERVICE
        )

        result = []
        MOCK_SCRAPER.when_get_then_return(LINKS[0])
        result.append(list(subject.process())[0])
        MOCK_SCRAPER.when_get_then_return(LINKS[1])
        result.append(list(subject.process())[0])
        MOCK_SCRAPER.when_get_then_return(LINKS[2])
        result.append(list(subject.process())[0])
        self.assertRaises(TypeError, list(subject.process()))
        self.assertEqual(LINKS, result)

if __name__ == '__main__':
    unittest.main()
