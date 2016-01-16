# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.core.files.uploadhandler import TemporaryFileUploadHandler


# copied from http://djangosnippets.org/snippets/678/

class ProgressBarUploadHandler(TemporaryFileUploadHandler):
    """
    Cache system for TemporaryFileUploadHandler
    """
    def __init__(self, *args, **kwargs):
        super(TemporaryFileUploadHandler, self).__init__(*args, **kwargs)
        self.progress_id = None
        self.cache_key = None
        self.original_file_name = None

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        self.content_length = content_length
        if 'X-Progress-ID' in self.request.GET:
            self.progress_id = self.request.GET['X-Progress-ID']
        elif 'X-Progress-ID' in self.request.META:
            self.progress_id = self.request.META['X-Progress-ID']
        if self.progress_id:
            self.cache_key = "%s_%s" % (self.request.META['REMOTE_ADDR'], self.progress_id)
            cache.set(self.cache_key, {
                'size': self.content_length,
                'received': 0
            }, 30)

    def new_file(self, field_name, file_name, content_type, content_length, charset=None, content_typ_extra=None):
        self.original_file_name = file_name

    def receive_data_chunk(self, raw_data, start):
        if self.cache_key:
            data = cache.get(self.cache_key, {})
            data['received'] += self.chunk_size
            cache.set(self.cache_key, data, 30)
        return raw_data

    def file_complete(self, file_size):
        pass

    def upload_complete(self):
        # deprecated in favor of setting an expiry time a-la-nginx
        # setting an expiry time fixes the race condition in which the last
        # progress request happens after the upload has finished meaning the
        # bar never gets to 100%
        pass
        #if self.cache_key:
        #    cache.delete(self.cache_key)
