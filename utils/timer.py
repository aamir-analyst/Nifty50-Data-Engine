import time


class Timer:

    def __init__(self):
        self.start = None

    def tic(self):
        self.start = time.time()

    def toc(self):

        elapsed = time.time() - self.start

        return round(elapsed, 2)