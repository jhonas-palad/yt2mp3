from django.apps import AppConfig


class YtConvertConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yt_convert'

    def ready(self):
        from . import signals