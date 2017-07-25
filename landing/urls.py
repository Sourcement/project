from django.conf.urls import url, include
from django.contrib import admin
from .views import landing

urlpatterns = [
    url(r'^$', landing, name='main')
]
