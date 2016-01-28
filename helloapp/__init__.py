
import time

print('Importing helloapp/__init__.py')

delay = 10
for i in range(delay):
    print('Slowly starting app.. {}/{}'.format(i+1, delay))
    time.sleep(1)
