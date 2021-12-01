from threading import Thread
import time


class ThreadManager(Thread):

    def __init__(self, *args, **kwargs):
        Thread.__init__(*args, **kwargs)
        self.start()

    def run(self) -> None:
        time.sleep(3)
