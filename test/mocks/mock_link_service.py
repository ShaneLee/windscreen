class MockLinkService:
    def __init__(self):
        self.count = None

    def process(self, html):
        return self.count

    def when_process_then_return(self, count):
        self.count = count

