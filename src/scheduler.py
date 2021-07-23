import random

class Scheduler:
    def __init__(self):
        self.called = False

    def delay_time(self):
        if not self.called:
            self.called = True
            return 0

        return random.randint(1, 10)
