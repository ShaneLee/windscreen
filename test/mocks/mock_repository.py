class MockRepository:
    def __init__(self):
        self.val = None
        
    def put(self, val):
        return val
        
    def put_all(self, vals):
        return len(vals)
    
    def get(self, key):
        return self.val

    def when_get_then_return(self, val):
        self.val = val
