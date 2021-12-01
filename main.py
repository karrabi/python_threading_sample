import time
import threadmanager as tm


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

    time.sleep(4)
    tm.UpdateGlobalVariable(new_value=50)


if __name__ == '__main__':
    main()
