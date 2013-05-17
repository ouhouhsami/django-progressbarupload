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


TEST_RUNNER = 'discover_runner.DiscoverRunner'

SECRET_KEY = 'very_secret_key'
