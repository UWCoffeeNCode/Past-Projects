import time
from typing import Dict, Tuple


class Timer:
    def __init__(self, duration: int):
        self.start_time = time.time()
        self.duration = duration

        self.remove = False

    def get_delta(self):
        if self.duration:
            delta = (time.time() - self.start_time) / self.duration
        else:  # Requiring 0 turns does not need animated position
            delta = 1

        return delta

    def is_done(self):
        return time.time() - self.start_time > self.duration
