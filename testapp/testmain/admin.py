# -*- coding: utf-8 -*-
from django.contrib import admin
from testmain.models import UploadFileModel, UploadFileModel2
from django import forms


class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel


class UploadFileModel2Inline(admin.TabularInline):
    model = UploadFileModel2


class UploadFileModelAdmin(admin.ModelAdmin):
    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'
    inlines = [UploadFileModel2Inline, ]
    form = UploadFileModelForm

    class Media:
        js = ("http://code.jquery.com/jquery.min.js",)


admin.site.register(UploadFileModel, UploadFileModelAdmin)
