from django.apps import AppConfig

class HelloworldConfig(AppConfig):
    name = 'helloworld'

    def ready(self):
        print('Running ready() on helloworld app')
