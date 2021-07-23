temp_batch_size = 10

class LocalLinkRepository:
    def __init__(self, config, provider):
        self.config = config
        self.batch_size = temp_batch_size
        self.links = set()

    def with_start_link(self, link):
        self.links.add(link)

    def put_all(self, val):
        self.links.update(val)
        return len(val)

    def get_batch(self):
        batch = []
        print('getting batch')
        for i in range(1, 10):
            try: 
                batch.append(self.links.pop())
            except KeyError:
                return batch
        return batch
