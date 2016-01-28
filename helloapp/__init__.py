
import random
import time

print('Importing helloapp/__init__.py')

delay = random.randint(2, 5)
for i in range(delay):
    print('Slowly starting app.. {}/{}'.format(i+1, delay))
    time.sleep(1)
