from django.conf.urls import url, include
from django.contrib import admin
from . import views
import sys
sys.path.append('..')


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join/$', views.join),
    url(r'^registration/$', views.registration, name='registration'), 
    url(r'^(?P<code>[a-zA-Z]{4})/$', views.room),
    #url(r'^(?P<code>[a-zA-Z]{4})/chat/$', views.chat),
    url(r'^about/', views.about, name='about'),
]
