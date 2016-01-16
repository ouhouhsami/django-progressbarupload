from django.test import TestCase
from django.core.cache import cache
from django.test.client import RequestFactory
from django.core.files.uploadhandler import load_handler
from time import sleep


class ProgressBarUploadHandlerTest(TestCase):
    def setUp(self):
        # set up request factory
        self.factory = RequestFactory()

    def test_progressbarhandler(self):
        progress_id = '1234'
        # fake request, just to get one, don't use post data
        request = self.factory.post('/?X-Progress-ID=%s' % progress_id)
        # instantiate progress bar upload handler with request
        h = load_handler(
            "progressbarupload.uploadhandler.ProgressBarUploadHandler",
            request)
        h.file_name = 'some_file.jpg'
        h.handle_raw_input('', h.request.META, 2 ** 24, 'bOuNdArY')
        self.assertIn(h.cache_key, cache)
        self.assertEqual(h.progress_id, '1234')
        self.assertEqual(h.cache_key, '127.0.0.1_1234')
        h.receive_data_chunk('a' * 65536, 1)
        # test if the cache is well filled
        self.assertEqual(cache.get(h.cache_key),
                         {'received': 65536, 'size': 16777216})
        h.upload_complete()
        # test if cache is cleared for the cache_key
        sleep(31)
        self.assertNotIn(h.cache_key, cache)
