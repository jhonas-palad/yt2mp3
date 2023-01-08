from django.db.models import signals
from django.dispatch import receiver
from .models import MP3Audio
from django.core.files.storage import default_storage

@receiver(signals.post_delete, sender = MP3Audio)
def delete_file(sender, instance, *args, **kwargs):
    """
    Delete the file associated to the MP3Audio object
    """
    file_path = instance.audio_file.path
    try:
        default_storage.delete(file_path)
    except Exception as err:
        print(f"Exception from post_delete signal: {err}")