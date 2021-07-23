import json
import redis
 
from src.models.article import ArticleEncoder

temp_hash = 'temp_articles'

class RedisRepository:
    def __init__(self, config, redis_provider):
        self.config = config
        self.hash_key = temp_hash
        self.redis = redis_provider.get()

    def put(self, val):
        json_val = json.dumps(val, cls=ArticleEncoder)
        return self.redis.hset(self.hash_key, val.get_url(), json_val)

    def get(self, key):
        return self.redis.hget(self.hash_key, key)
