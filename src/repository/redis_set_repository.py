import redis

temp_set = 'temp_links'
temp_batch_size = 10

class RedisSetRepository:
    def __init__(self, config, redis_provider):
        self.config = config
        self.set_key = temp_set
        self.batch_size = temp_batch_size
        self.redis = redis_provider.get()

    def put_all(self, val):
        return len(
            list(
                map(lambda x: self.redis.zadd(self.set_key, x, 1), val)
            ))

    def get_batch(self):
        batch = self.redis.zrangebyscore(
            self.set_key, 
            1, 
            1,
            start=0,
            num=self.batch_size)

    def _mark_as_seen(self, vals):
        list(
            map(lambda x: self.redis.zrem(self.set_key, x), val)
        )
        return len(
            list(
                map(lambda x: self.redis.zadd(self.set_key, x, -1), val)
            ))
        
