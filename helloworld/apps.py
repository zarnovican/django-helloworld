import os
import time

from django.apps import AppConfig

print('importing helloworld/app.py')

class HelloworldConfig(AppConfig):
    name = 'helloworld'

    def ready(self):
        print('Running ready() on helloworld app')
        delay = 5
        for i in range(delay):
            print('pid {}: Slowly starting app.. {}/{}'.format(os.getpid(), i+1, delay))
            time.sleep(1)
