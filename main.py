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
    
    for name, seconds in threadlist.items():
        # print('name: {} and seconds is {}'.format(name, seconds))
        thread = tm.ThreadManager(name=name, seconds=seconds)


if __name__ == '__main__':
    main()
