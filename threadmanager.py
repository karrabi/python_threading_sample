from threading import Thread
import time


global_sum = 0

class ThreadManager(Thread):

    def __init__(self, *args, **kwargs):
        Thread.__init__(self)

        if 'name' in kwargs:
            self.name = kwargs.get('name')
        else:
            self.name = 'Unknown'

        if 'seconds' in kwargs:
            self.seconds = kwargs.get('seconds')
        else:
            self.seconds = 0

        self.start()

    def run(self) -> None:
        global global_sum
        print('{} thread fall asleep for {} seconds'.format(self.name, self.seconds))
        time.sleep(self.seconds)
        global_sum += self.seconds
        print('{} thread finished. global sum is {}'.format(self.name, global_sum))

