class MockGenerator(object):
    def __init__(self, iterable):
        self.num = 0
        self.iterable = iterable
        self.n = len(self.iterable)

    def __iter__(self):
         return self

    def __next__(self):
         return self.next()

    def next(self):
         if self.num < self.n:
             cur, self.num = self.num, self.num+1
             return self.iterable[cur]
         raise StopIteration()
