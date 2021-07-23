class MockArticleFactory:
    def __init__(self):
        self.val = None
        
    def create(self, html):
        return self.val
        
    def when_create_then_return(self, val):
        self.val = val
