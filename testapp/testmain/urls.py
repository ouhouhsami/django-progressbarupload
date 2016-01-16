# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import FormView
from testmain import views
from testmain.forms import UploadForm

urlpatterns = patterns('',
                       url(r'^form/', FormView.as_view(form_class=UploadForm,
                                                       template_name="testmain/form.html",
                                                       success_url="/testapp/form")),
                       url(r'^modelform/', views.upload_modelform, name='modelform')
)
