from django.conf.urls import url, include
from django.contrib import admin
from .views import vfunc

urlpatterns = [
    url(r'^$', vfunc, name='main')
]
