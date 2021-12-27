import os
import sys
import multiprocessing
import datetime
import time
import signal

def runner(q):
    while True:
        cmd = q.get()
        print('run command : {}'.format(cmd))
        if cmd is None:
            break
        code = os.system(cmd)
        print('command exit code : {}'.format(code))
        q.task_done()

def main(argv):
    print('[start time] {}'.format(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))
    worker_num = argv[0]
    print('worker_num : {}'.format(worker_num))
    cmd_num = argv[1]
    print('cmd_num : {}'.format(cmd_num))

    cmd_list = []
    for _ in range(int(cmd_num)):
        cmd = 'python _multiprocess.py {}'.format(_)
        cmd_list.append(cmd)

    queue = multiprocessing.JoinableQueue()
    ps = []
    for _ in range(int(worker_num)):
        p = multiprocessing.Process(target=runner, args=(queue,))
        p.start()
        ps.append(p)

    def term_handler(sig, frame):
        for p in ps:
            os.kill(p.pid, signal.SIGTERM)
        raise Exception("ctrl + c exit")

    signal.signal(signal.SIGINT, term_handler)

    for cmd in cmd_list:
        queue.put(cmd)

    queue.join()

    for p in ps:
        os.kill(p.pid, signal.SIGTERM)

    print('[end time] {}'.format(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')))

if __name__ == '__main__':
    try:
        print('train start')
        main(sys.argv[1:])
    except Exception as e:
        print('[ERROR] {}'.format(e))
        raise
    finally:
        print('train finish')
