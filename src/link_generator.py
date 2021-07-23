class LinkGenerator:
    def __init__(self, repository, scheduler):
        self.repository = repository
        self.scheduler = scheduler
        self.called = False
        self.batch = []

    def __iter__(self):
         return self

    def __next__(self):
         return self.next()

    def next(self): 
         if self.batch:
            return self.batch.pop()
         if not self.called:
            self.called = True
         if self.called:
            self.batch = self.repository.get_batch()
            return self.batch.pop()
         raise StopIteration()
