from django.db import models
from typing import Dict

class TimeStampedModel(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MP3Audio(TimeStampedModel):
    youtube_id = models.CharField(primary_key=True, max_length=100)
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    length = models.IntegerField()
    abr = models.CharField(max_length=100, null=True)
    audio_file = models.FileField(upload_to='%Y/%m/%d')
    
    class Meta:
        verbose_name = 'MP3Audio'

    def new_updates(self, **kwargs):
        for attr, val in kwargs.items():
            if getattr(self, attr) != val:
                setattr(self, attr, val)
        self.save()

