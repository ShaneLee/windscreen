MESSAGE = 'Missing arguments exception: \n\n'

class MissingArgsException(Exception):
    def __init__(self, message):
        self.message = MESSAGE + message
        super().__init__(self.message)
