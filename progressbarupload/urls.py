# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from views import upload_progress

urlpatterns = patterns('',
    url(r'^upload_progress$', upload_progress, name="upload_progress"),
)
