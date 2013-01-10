import uuid
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django import template
from django.forms.widgets import Media

register = template.Library()


@register.simple_tag
def progress_bar():
    """
    progress_bar simple tag

    return html5 tag to display the progress bar
    and url of ajax function needed to get upload progress
    in js/progress_bar.js file.
    """
    prograss_bar_tag = '<progress id="progressBar" ' \
        'data-progress_bar_uuid="%s" value="0" max="100" ' \
        'hidden></progress>' % (uuid.uuid4())
    upload_progress_url = '<script>upload_progress_url = "%s"</script>' \
        % (reverse('upload_progress'))
    return mark_safe(prograss_bar_tag + upload_progress_url)


@register.simple_tag
def progress_bar_media():
    """
    progress_bar_media simple tag

    return rendered script tag for javascript used by progress_bar
    """
    m = Media(js=["http://code.jquery.com/jquery-1.8.3.min.js",
        "js/progress_bar.js"])
    return m.render()
