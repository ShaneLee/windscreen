from test.mocks.mock_redis import MockRedis

class RedisProvider:
    def __init__(self):
        self.redis = MockRedis()

    def get(self):
        return self.redis

