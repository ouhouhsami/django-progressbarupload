# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core.cache import cache

try:
    import json
except ImportError:
    # Django <1.7 packages simplejson for older Python versions
    from django.utils import simplejson as json


def upload_progress(request):
    """
    Used by Ajax calls

    Return the upload progress and total length values
    """
    if 'X-Progress-ID' in request.GET:
        progress_id = request.GET['X-Progress-ID']
    elif 'X-Progress-ID' in request.META:
        progress_id = request.META['X-Progress-ID']
    else:
        progress_id = None

    if progress_id:
        cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], progress_id)
        data = cache.get(cache_key)
        return HttpResponse(json.dumps(data))
