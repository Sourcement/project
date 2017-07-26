from django.conf.urls import url, include
from django.contrib import admin
from .views import landing, contact_form


app_name = 'landing'

urlpatterns = [
    url(r'^$', landing, name='main_landing'),
    url(r'^send_mail/$', contact_form),
]
