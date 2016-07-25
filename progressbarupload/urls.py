# -*- coding: utf-8 -*-
from django.conf.urls import url
from progressbarupload.views import upload_progress

urlpatterns = [
    url(r'^upload_progress$', upload_progress, name="upload_progress"),
]
