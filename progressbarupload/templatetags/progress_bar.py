import uuid

from django import template
from django.conf import settings
from django.forms.widgets import Media
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def progress_bar():
    """
    progress_bar simple tag

    return html5 tag to display the progress bar
    and url of ajax function needed to get upload progress
    in js/progress_bar.js file.
    """
    progress_bar_tag = '<progress id="progressBar" ' \
        'data-progress_bar_uuid="%s" style="width:100%%" value="0" max="100" ' \
        'hidden></progress>' % (uuid.uuid4())
    upload_progress_url = '<script>upload_progress_url = "%s"</script>' \
        % (reverse('upload_progress'))
    return mark_safe(progress_bar_tag + upload_progress_url)


@register.simple_tag
def progress_bar_media():
    """
    progress_bar_media simple tag

    return rendered script tag for javascript used by progress_bar
    """
    include_jquery = getattr(settings, 'PROGRESSBARUPLOAD_INCLUDE_JQUERY', False)

    if include_jquery:
        js = ["//code.jquery.com/jquery-1.12.0.min.js"]
    else:
        js = []
    js.append("js/progress_bar.js")

    m = Media(js=js)
    return m.render()
