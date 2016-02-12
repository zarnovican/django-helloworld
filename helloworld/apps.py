from django.apps import AppConfig

print('importing helloworld/app.py')

class HelloworldConfig(AppConfig):
    name = 'helloworld'

    def ready(self):
        print('Running ready() on helloworld app')
