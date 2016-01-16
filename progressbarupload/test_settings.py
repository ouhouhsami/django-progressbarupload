SITE_ID = 1

FILE_UPLOAD_MAX_MEMORY_SIZE = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'progressbarupload',
    }
}

FILE_UPLOAD_HANDLERS = (
    "progressbarupload.uploadhandler.ProgressBarUploadHandler",
)

SECRET_KEY = 'very_secret_key'


try:
    from progressbarupload._local_tests import *
except ImportError, e:
    print u"FYI: You have no progressbarupload/_local_tests.py, but you should!"
    pass
