from django.apps import AppConfig


class LoginConfig(AppConfig):
    name = 'login'

    # def ready(self):
    #     from login.core import scheduler
    #     scheduler.start()
