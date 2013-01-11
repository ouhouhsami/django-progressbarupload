========================
django-progressbarupload
========================

django-progressbarupload is a simple Django application that instantiates an HTML5 upload progress bar when the user submit a form with files (a form having basically FileField(s) and/or ImageField(s), and an enctype="multipart/form-data").

![ScreenShot](https://raw.github.com/ouhouhsami/django-progressbarupload/master/docs/img/admin_progress_bar_screenshot.png)


Quick start
-----------

Requirements : 
* Django 1.4.3 (tested).
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


