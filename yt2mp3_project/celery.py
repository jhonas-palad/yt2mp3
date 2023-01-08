import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yt2mp3_project.settings')

app = Celery('yt2mp3_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

# automatically find all tasks in each app of your Django project.
app.autodiscover_tasks()

