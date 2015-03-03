# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from progressbarupload import views

urlpatterns = patterns('',
    url(r'^upload_progress$', views.upload_progress, name="upload_progress"),
)
