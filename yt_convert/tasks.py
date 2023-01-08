import os
import shutil
import uuid

from . import utils
from pytube import YouTube, Stream
from pytube.exceptions import PytubeError, RegexMatchError
from typing import Dict, Any
from io import BytesIO

from django.urls import reverse
from django.conf import settings
from django.core.files.base import File
from .models import MP3Audio

def fetch_yt_info(url: str) -> Dict[str, Any]:
    result : Dict = {}
    try:
        yt = YouTube(str(url))
        yt.check_availability()
    except RegexMatchError:
        result['err_msg'] = 'Invalid youtube url'
    except PytubeError as pytube_err:
        result['err_msg'] = pytube_err.error_string \
            if hasattr(pytube_err, 'error_string')  \
            else 'An error occured while fetching the YouTube Video'
    else:
        keys = (
            'video_id',
            'title', 
            'author', 
            'length', 
            'publish_date',
            'thumbnail_url',
            'streams'
        )
        result.update({k : getattr(yt, k) for k in keys})

    return result

def download_audio(audio: Stream) -> File:
    output_filename = utils.create_mp3_filename(audio.title)
    uniq_filename = f'{uuid.uuid4().hex}_{output_filename}'

    buffer = BytesIO()
    audio.stream_to_buffer(buffer)

    return File(buffer, name = uniq_filename)

def extract_audio(url: str) -> Dict[str, Any]:
    yt_info : Dict[str, Any]

    yt_info = fetch_yt_info(url)

    if 'err_msg' in yt_info:
        # Return immediately, it doesn't have the information we need.
        return yt_info

    audio_stream = yt_info.pop('streams').get_audio_only()
    keyword_args = {
        'youtube_id': yt_info['video_id'],
        'url': url,
        'title': yt_info['title'],
        'length': yt_info['length'],
        'abr': audio_stream.abr
    }
    try:
        mp3_audio = MP3Audio.objects.get(youtube_id = yt_info['video_id'])
    except MP3Audio.DoesNotExist:
        #Get the highest bitrate audio stream
        audio_file = download_audio(audio_stream)
        mp3_audio = MP3Audio(
            **keyword_args,
            audio_file = audio_file,
        )
        if mp3_audio:
            mp3_audio.save()
            
        else:
            yt_info['err_msg'] = 'Something went wrong: DATABASE'
    else:
        """
        Try to update
        """
        mp3_audio.new_updates(**keyword_args)
    yt_info['abr'] = audio_stream.abr
    yt_info['filesize_mb'] = getattr(audio_stream, 'filesize_mb', 'UNKNOWN')
    yt_info['dl_url'] = reverse("yt_convert:download", kwargs={'youtube_id': yt_info['video_id']})
    
    return yt_info

