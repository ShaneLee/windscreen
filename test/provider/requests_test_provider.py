from test.mocks.mock_requests import MockRequests

class RequestsProvider:
    def __init__(self):
        self.requests = MockRequests()

    def get(self):
        return self.requests

