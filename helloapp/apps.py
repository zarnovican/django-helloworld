from django.apps import AppConfig

print('Importing helloapp/apps.py')

class HelloappConfig(AppConfig):
    name = 'helloapp'

    def ready(self):
        print('Running ready() on helloapp')
