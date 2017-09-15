from django.conf.urls import url, include
from django.contrib import admin
from . import views
import sys
sys.path.append('..')


urlpatterns = [
    url(r'^$', views.index),
    url(r'^join/$', views.join),
    url(r'^registration/$', views.registration), 
    url(r'^(?P<code>[a-zA-Z]{4})/$', views.room),
    url(r'^about/', views.about),
]
