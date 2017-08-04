from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from . import views
import sys
sys.path.append('..')

"""
Viewsets
"""
from api.viewsets.rooms import RoomViewSet

"""
Automatically determine the URL conf
"""
router = routers.DefaultRouter()
router.register(r'room', RoomViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join/$', views.join),
    url(r'^registration/$', views.registration, name='registration'), 
    url(r'^(?P<code>[a-zA-Z]{4})/$', views.room),
    url(r'^(?P<code>[a-zA-Z]{4})/chat/$', views.chat),
    url(r'^about/', views.about, name='about'),
    url(r'^api/v1/', include(router.urls)),
   # url(r'^', include('rest_framework.urls', namespace='rest_framework')),
]
