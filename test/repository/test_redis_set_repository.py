import unittest

from src.repository.redis_set_repository import RedisSetRepository

from test.provider.redis_test_provider import RedisProvider

MOCK_REDIS_PROVIDER = RedisProvider()
MOCK_REDIS = MOCK_REDIS_PROVIDER.get()

subject = RedisSetRepository(None, MOCK_REDIS_PROVIDER)

URL = 'http://www.example.com'

LINKS = ['1','2','3']

class TestRedisSetRepository(unittest.TestCase):
    def test_put_all(self):
       self.assertEqual(3, subject.put_all(LINKS))

if __name__ == '__main__':
    unittest.main()
