import redis

class RedisProvider:
    def __init__(self):
        pass

    def get(self):
        return redis.StrictRedis()

