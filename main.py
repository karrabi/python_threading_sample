import time
import threadmanager as tm
import watcher

threadlist = {
        'first': 1,
        'second': 2,
        'third': 3,
        'fourth': 4,
        'fifth': 5,
        'sixth': 6
}


def main():
    threads = [tm.ThreadManager(name=name, seconds=seconds) for name, seconds in threadlist.items()]

    watch = watcher.Watch()


if __name__ == '__main__':
    main()
