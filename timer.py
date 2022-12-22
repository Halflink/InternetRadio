import time


class Timer:

    def __init__(self):

        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def get_elapsed_time(self):
        return time.perf_counter() - self.start_time

    def stop(self):
        elapsed_time = self.get_elapsed_time()
        self.start_time = None
        return elapsed_time

    def has_time_elapsed(self, seconds):
        if self.start_time is None:
            return False
        elif self.get_elapsed_time() > seconds:
            return True
        else:
            return False


