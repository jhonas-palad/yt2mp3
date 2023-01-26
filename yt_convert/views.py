import json

from django.conf import settings
from django.http import JsonResponse, FileResponse, HttpResponse
from django.views.generic import TemplateView
from django.views import View
from .models import MP3Audio
from django.core.exceptions import ObjectDoesNotExist

from .forms import YTUrlForm
from . import tasks

from typing import Any, Dict


class HomeView(TemplateView):
    template_name = 'yt_convert/home_v2.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['yt_url_form'] = YTUrlForm()
        context['debug_mode'] = settings.DEBUG
        return context
    
class ConvertView(View):

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """
        fetch api request
        """
        response : JsonResponse
        status_code: int = 200
        data: Dict[str, str] = {}

        post_data = json.loads(request.body)
        bound_form = YTUrlForm(post_data)
        if bound_form.is_valid():
            url: str = bound_form.cleaned_data['yt_url']
            res: Dict = tasks.extract_audio.delay(url)
            extracted_audio_info = res.get()
            if 'err_msg' in extracted_audio_info:
                data['err_msg'] = extracted_audio_info['err_msg']
                status_code = 400
            else:
                data.update(extracted_audio_info)
        else:
            data['err_msg'] = 'Invalid YouTube URL'
            status_code = 400

        response = JsonResponse(data, status=status_code)
        return response

class DownloadView(View):
    def get(self, request, youtube_id, *args, **kwargs):
        try:
            mp3_audio = MP3Audio.objects.get(youtube_id = youtube_id)
        except MP3Audio.DoesNotExist:
            mp3_audio = None
        if mp3_audio:
            audio_file = mp3_audio.audio_file
            response = FileResponse(audio_file, as_attachment=True)
        else:
            response = HttpResponse('FAULT PAGE')

        return response
