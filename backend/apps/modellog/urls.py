#coding:utf-8
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'logsentrys', LogsEntryViewSet, base_name='logsentry')
router.register(r'models', ContentTypeViewSet, base_name='model')

urlpatterns = router.urls
