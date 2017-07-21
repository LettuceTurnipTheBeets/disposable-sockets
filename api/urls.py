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
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
   # url(r'^', include('rest_framework.urls', namespace='rest_framework')),
]
