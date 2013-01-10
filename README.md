========================
django-progressbarupload
========================

django-progressbarupload is a simple Django application that instantiate an html5 progress bar on ModelAdmin change form to show upload progression of all files in request.FILES (FileField and ImageField on models).

![ScreenShot](https://raw.github.com/ouhouhsami/django-progressbarupload/master/docs/img/admin_progress_bar_screenshot.png)

django-progressbarupload is tested under django 1.4.3. To work, it needs django.contrib.staticfiles app to serve static files (progress_bar.js).


Quick start
-----------

0. Install the app

	```
	pip install -e git+http://github.com/ouhouhsami/django-progressbarupload.git#egg=django-progressbarupload
	```

1. Add "progressbarupload.uploadhandler.ProgressBarUploadHandler" to your FILE_UPLOAD_HANDLERS setting like this:: 

	```python
	FILE_UPLOAD_HANDLERS = (
	    "progressbarupload.uploadhandler.ProgressBarUploadHandler",
	    "django.core.files.uploadhandler.MemoryFileUploadHandler",
	    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
	)
	```

2. Include the progressbarupload URLconf in your project urls.py like this::

	```
    (r'^progressbarupload/', include('progressbarupload.urls')),
    ```

3. Use progressbarupload.admin.ProgressBarModelAdmin as base class for your ModelAdmin on which you want to have a progress bar.

	```python
	from django.contrib import admin
	from progressbarupload.admin import ProgressBarModelAdmin
	from my_awesome_app.models import MyAwesomeModelWithFiles

	class MyAwesomeModelWithFiles(ProgressBarModelAdmin):
	    pass

	admin.site.register(MyAwesomeModelWithFiles, UploadFileModelAdmin)
	```

Further information
-------------------

Make sure your browser renders html5 <progress> tag and use data-* attribute (IE>10, FF>6.0, Chrome>8.0, Opera>11.0).

As Django has a unique TemporaryFileUploadHandler for all request.FILES, if you have related models, using TabularInline, the upload progress will be also shown in the admin add/change form as soon as you use ProgressBarModelAdmin in place of your ModelAdmin (and even if your ProgressBarModelAdmin doesn't contain any file upload).

Custom TemporaryFileUploadHandler copied from http://djangosnippets.org/snippets/678/


