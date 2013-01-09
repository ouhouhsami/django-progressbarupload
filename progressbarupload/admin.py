# -*- coding: utf-8 -*-
import uuid

from django.contrib import admin
from progressbarupload.models import UploadFileModel, UploadFileModel2


class ProgressBarModelAdmin(admin.ModelAdmin):
    """
    Base class for ModelAdmin which require a progress bar for upload
    """

    change_form_template = "progressbarupload/change_form.html"

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['uuid'] = uuid.uuid4()
        return super(ProgressBarModelAdmin, self).change_view(request,
            object_id, form_url, extra_context)

    class Media:
        js = ("http://code.jquery.com/jquery-1.8.3.min.js",
            "js/progress_bar.js",)


class UploadFileModel2Inline(admin.TabularInline):
    model = UploadFileModel2


class UploadFileModelAdmin(ProgressBarModelAdmin):

    inlines = [UploadFileModel2Inline, ]


admin.site.register(UploadFileModel, UploadFileModelAdmin)
