# -*- coding: utf-8 -*-
from django.db import models


class UploadFileModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField()
    file2 = models.FileField()

    def __unicode__(self):
        return self.name


class UploadFileModel2(models.Model):
    ufm = models.ForeignKey(UploadFileModel)
    file = models.FileField()
