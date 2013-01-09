=================
ProgressBarUpload
=================

ProgressBarUpload is a simple Django application that instantiate an html5 progress bar on ModelAdmin change form
to show upload progression of all files in request.files (FileField and ImageField on models).

Quick start
-----------

1. Add "progressbarupload.uploadhandler.ProgressBarUploadHandler" to your FILE_UPLOAD_HANDLERS setting like this:: 

	FILE_UPLOAD_HANDLERS = (
	    "progressbarupload.uploadhandler.ProgressBarUploadHandler",
	    "django.core.files.uploadhandler.MemoryFileUploadHandler",
	    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
	)

2. Include the progressbarupload URLconf in your project urls.py like this::

    (r'^progressbarupload/', include('progressbarupload.urls')),

3. Use progressbarupload.admin.ProgressBarModelAdmin as base class for your ModelAdmin on which you want to have a progress bar.