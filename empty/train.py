import os, sys, time

print('>>>>>> print argv')
for arg in sys.argv:
    print('Arg Value = ', arg)

print('>>>>>> print env variables')
for a in os.environ:
    print(a, '=', os.getenv(a))

sleep_time = os.getenv('sleep',600)
print('>>>>>> sleep_time : {}s'.format(sleep_time))
time.sleep(sleep_time)
print('>>>>>> done')