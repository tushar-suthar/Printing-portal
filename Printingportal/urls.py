from . import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', views.main, name='main'),
    url(r'^home/',include('home.urls')),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft')),
    path('admin/', admin.site.urls),
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('callback', views.callback, name='callback'),
]
