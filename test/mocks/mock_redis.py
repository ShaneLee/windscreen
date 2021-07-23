class MockRedis:
    def __init__(self):
        self.val = None

    def hset(self, hash_key, field_key, val):
        return 1

    def hget(self, hash_key, field_key):
        return self.val

    def when_hget_then_return(self, val):
        self.val = val

    def zadd(self, set_key, val, score):
        return 1

