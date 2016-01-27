from django.apps import AppConfig

print('Importing helloapp/apps.py')

class HelloappConfig(AppConfig):
    name = 'helloapp'
    foo = 'bar'
