
import os
import time

print('Importing helloapp/__init__.py')

delay = 10
for i in range(delay):
    print('pid {}: Slowly starting app.. {}/{}'.format(os.getpid(), i+1, delay))
    time.sleep(1)
