from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'yt_convert'

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('fetch_yt/', csrf_exempt(views.ConvertView.as_view())),
    path('download/<str:youtube_id>', views.DownloadView.as_view(), name = 'download')
]