from django.conf.urls import url
from django.contrib import admin
from api.views import index1
#wghtest
#wghtestNO2update

urlpatterns = [
    url(r'^', index1),
]
