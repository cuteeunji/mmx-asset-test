import sys

def main(argv):
    loop_num = argv[0]
    print('loop_num : {}'.format(loop_num))
    for _ in range(int(loop_num)):
        print('in loop {}'.format(_))

if __name__ == '__main__':
    print('script start')
    main(sys.argv[1:])
    print('script finish')
