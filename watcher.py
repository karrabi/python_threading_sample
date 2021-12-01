import time
from threading import Thread
import threadmanager as tm


class Watch(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self) -> None:

        while True:
            if tm.global_sum > 10:
                tm.global_sum = 0
                print('GLOBAL VARIABLE global_sum RESET TO 0')

