from django.test import TestCase
from django.core.cache import cache
from django.test.client import RequestFactory
from django.core.files.uploadhandler import load_handler


class ProgressBarUploadHandlerTest(TestCase):
    def setUp(self):
        # set up request factory
        self.factory = RequestFactory()

    def test_progressbarhandler(self):
        progress_id = '1234'
        # fake request, just to get one, don't use post data
        request = self.factory.post('/?X-Progress-ID=%s' % progress_id)
        # instanciate progress bar upload handler with request
        h = load_handler(
            "progressbarupload.uploadhandler.ProgressBarUploadHandler",
            request)
        h.handle_raw_input('', h.request.META, 2 ** 24, 'bOuNdArY')
        self.assertTrue(h.cache_key in cache)
        self.assertTrue(h.progress_id == '1234')
        self.assertTrue(h.cache_key == '127.0.0.1_1234')
        h.receive_data_chunk('a' * 65536, 1)
        # test if the cache is well filled
        self.assertTrue(cache.get(h.cache_key) ==
            {'uploaded': 65536, 'length': 16777216})
        h.upload_complete()
        # test if cache is cleared for the cache_key
        self.assertFalse(h.cache_key in cache)
