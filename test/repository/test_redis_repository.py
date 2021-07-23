import unittest

from src.builder.metadata_builder import MetadataBuilder
from src.repository.redis_repository import RedisRepository

from test.provider.redis_test_provider import RedisProvider

MOCK_REDIS_PROVIDER = RedisProvider()
MOCK_REDIS = MOCK_REDIS_PROVIDER.get()

subject = RedisRepository(None, MOCK_REDIS_PROVIDER)

URL = 'http://www.example.com'
AUTHOR = 'Leeroy Jenkins'


class TestParser(unittest.TestCase):
    def test_put(self):
       val = MetadataBuilder(False).with_url(URL).with_author(AUTHOR).build() 
       self.assertEqual(1, subject.put(val))

    def test_get(self):
       val = MetadataBuilder(False).with_url(URL).with_author(AUTHOR).build() 
       MOCK_REDIS.when_hget_then_return(val)
       self.assertEqual(val, subject.get(URL))

if __name__ == '__main__':
    unittest.main()
