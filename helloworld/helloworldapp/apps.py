from django.apps import AppConfig


class HelloworldappConfig(AppConfig):
    name = 'helloworldapp'

    def ready(self):
        print('hello from ready')
