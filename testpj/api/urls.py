from django.conf.urls import url
from django.contrib import admin
from api.views import index
#wghtest

urlpatterns = [
    url(r'^', index),
]
