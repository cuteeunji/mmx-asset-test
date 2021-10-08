import os, sys, time

print('>>>>>> print argv')
for arg in sys.argv:
    print('Arg Value = ', arg)

print('>>>>>> print env variables')
for a in os.environ:
    print(a, '=', os.getenv(a))

sleep_time = os.getenv('sleep',180)

for i in range(1, int(sleep_time)):
    time.sleep(1)
    print('>>>>>> sleep_time : {}s'.format(i))

print('>>>>>> done')