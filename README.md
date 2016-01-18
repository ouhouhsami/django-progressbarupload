========================
django-progressbarupload
========================

[![Build Status](https://travis-ci.org/ouhouhsami/django-progressbarupload.png?branch=master)](https://travis-ci.org/ouhouhsami/django-progressbarupload)

django-progressbarupload is a simple Django application that instantiates an HTML5 upload progress bar when the user submits a form with files (a form having basically FileField(s) and/or ImageField(s), and an enctype="multipart/form-data").

![ScreenShot](https://raw.github.com/ouhouhsami/django-progressbarupload/master/docs/img/admin_progress_bar_screenshot.png)

###Contributors
The following users have contributed:
* [Iago Suárez](https://github.com/iago-suarez)
* [Andrew Brookins](https://github.com/abrookins)
* [Callan Bryant](https://github.com/naggie)
* [Mathieu Comandon](https://github.com/strycore)

Quick start
-----------

Requirements :
* Django 1.7.4 or above.
* Python 2.7 or 3.4
* django.contrib.staticfiles app to serve static files


1. Install the app

    pypi version

    ```
    pip install django-progressbarupload
    ```

    development version

    ```
    pip install -e git+http://github.com/ouhouhsami/django-progressbarupload.git#egg=django-progressbarupload
    ```

2. Add progressbarupload to your INSTALLED_APPS in your settings

    ```
    INSTALLED_APPS += ('progressbarupload', )
    ```

3. Add "progressbarupload.uploadhandler.ProgressBarUploadHandler" to your FILE_UPLOAD_HANDLERS setting

    ```python
    FILE_UPLOAD_HANDLERS = (
        "progressbarupload.uploadhandler.ProgressBarUploadHandler",
        "django.core.files.uploadhandler.MemoryFileUploadHandler",
        "django.core.files.uploadhandler.TemporaryFileUploadHandler",
    )
    ```

4. Include the progressbarupload URLconf in your project urls.py

    ```
    (r'^progressbarupload/', include('progressbarupload.urls')),
    ```

5. In your settings file, if you don't want to include jquery with {% progress_bar_media %}, then set:

    ``` python
    PROGRESSBARUPLOAD_INCLUDE_JQUERY = False
    ```

Usage
-----

### ModelAdmin

Set the ```change_form_template``` and ```add_form_template``` attributes in your ModelAdmin to 'progressbarupload/change_form.html'.


    from django.contrib import admin
    from my_awesome_app.models import MyAwesomeModelWithFiles

    class MyAwesomeModelWithFiles(admin.ModelAdmin):
        change_form_template = 'progressbarupload/change_form.html'
        add_form_template = 'progressbarupload/change_form.html'

    admin.site.register(MyAwesomeModelWithFiles, UploadFileModelAdmin)

Demo
----

This app includes a demo app, just go inside testapp dir and run

    python manage.py migrate
    python manage.py runserver

then go to http://127.0.0.1:8000/admin or http://127.0.0.1:8000/admin http://127.0.0.1:8000/testapp/form or http://127.0.0.1:8000/testapp/modelform


### Form and ModelForm

To use a progress bar in your custom ModelForm or Form, load the progress_bar template tag set ```{% load progress_bar %}``` in the template, and use the following template tags ```{% progress_bar_media %}``` between <head> tags to load javascript files and  ```{% progress_bar %}``` where you and to display the progress bar.


    {% load progress_bar %}

    <!DOCTYPE html>
    <html>
    <head>
        {% progress_bar_media %}
    </head>

    <body>
      <form enctype="multipart/form-data" method="post" action=".">
         {% csrf_token %}
         {{ form }}
         {% progress_bar %}
         <input type="submit" />
     </form>
    </body>
    </html>


Further information
-------------------

Make sure your browser renders HTML5 ```<progress>``` tag and uses data-* attribute (IE>10, FF>6.0, Chrome>8.0, Opera>11.0).

As Django has a unique TemporaryFileUploadHandler for all request.FILES. For ModelAdmin, if you have related models, using TabularInline, the upload progress will also be shown in the admin add/change form as soon as you use the right templates in your ModelAdmin (and even if your ModelAdmin doesn't contain any file upload).

Custom TemporaryFileUploadHandler copied from http://djangosnippets.org/snippets/678/

Launch tests
------------

It assumes you have installed virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/)

```
# get the application code
git clone https://github.com/ouhouhsami/django-progressbarupload.git
cd django-progressbarupload
# create a virtualenv
mkvirtualenv progressbarupload
add2virtualenv .
# install requirements for tests and django (set the django version you want to use)
pip install -r requirements/tests.txt django==1.7.4
# launch tests
django-admin.py test --settings=progressbarupload.test_settings progressbarupload
```

=======
New: Use transparently with uwsgi/nginx
---------------------------------------
The combination of uwsgi and nginx prevent django-progressbarupload from
working because nginx buffers the entire POST request until it is complete
before sending it to uwsgi/django. This means your application runs faster as
uwsgi threads are less tied up, but it also makes it impossible to view to
progress Django side.

Whilst you could use XMLHttpRequest 2.0 to get the progress client-side, you
may not have the luxury if you need to support older browsers. This is where
[RFC1867][2] comes in. By configuring the [nginx-upload-progress-module][1] in
the following way, it is possible to transparently support the native method as
well as the plugin:

```
	...
	upload_progress uploadp 1m;
	# JSON document rather than JSONP callback, pls
	upload_progress_json_output;
	...
	location ^ upload/url/pattern/
	    track_uploads uploadp 30s {
	}
	...
	location ^~ /progressbarupload/upload_progress {
	    report_uploads uploadp;
	}

```

nginx-upload-progress-module is available on ubuntu in the `nginx-extras` package.

[1]: https://github.com/masterzen/nginx-upload-progress-module
[2]: http://www.rfcreader.com/#rfc1867
