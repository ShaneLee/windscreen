from src.content_service import ContentService
from src.config.config import Config
from src.link_generator import LinkGenerator
from src.link_service import LinkService
from src.processor import Processor
from src.factory.article_factory import ArticleFactory
from src.provider.redis_provider import RedisProvider
from src.provider.requests_provider import RequestsProvider
from src.parser import Parser
from src.repository.local_link_repository import LocalLinkRepository
from src.repository.redis_repository import RedisRepository
from src.scheduler import Scheduler
from src.scraper import Scraper

SCHEDULER = Scheduler()
REDIS_PROVIDER = RedisProvider()
REQUESTS_PROVIDER = RequestsProvider()
LINK_REPOSITORY = LocalLinkRepository(None, None)
ARTICLE_REPOSITORIY = RedisRepository(None, REDIS_PROVIDER)
LINK_GENERATOR = LinkGenerator(LINK_REPOSITORY, SCHEDULER)
SCRAPER = Scraper(REQUESTS_PROVIDER)
PARSER = Parser()
LINK_SERVICE = LinkService(PARSER, LINK_REPOSITORY)
ARTICLE_FACTORY = ArticleFactory(PARSER)
CONTENT_SERVICE = ContentService(ARTICLE_FACTORY, ARTICLE_REPOSITORIY)
CONFIG = Config()

def main():
    print('Starting scraper')
    start_link = 'https://amp.ft.com/content/136930dc-16cb-4acc-bdee-09833697244b'
    LINK_REPOSITORY.with_start_link(start_link)
    processor = Processor(
        CONFIG,
        SCHEDULER, 
        LINK_GENERATOR,
        SCRAPER,
        CONTENT_SERVICE,
        LINK_SERVICE
    )
    while (True):
        try: 
            processor.process().__next__()
        except:
            processor.process().__next__()

if __name__ == '__main__':
    main()
