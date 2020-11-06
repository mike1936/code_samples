# my_project/my_app/urls.py
from django.urls import path, include
from rest_framework import routers

from my_app.views import MyViewSets

router = routers.DefaultRouter()
router.register('test', MyViewSets)

urlpatterns = [
    path('', include(router.urls))
]
