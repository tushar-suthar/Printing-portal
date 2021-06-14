from . import views
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$',views.home),
    url(r'^success',views.success),
    path('upload', views.upload_multiple_files, name='upload_multiple_files'),
]