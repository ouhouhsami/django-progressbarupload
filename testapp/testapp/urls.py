from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^testapp/', include('testmain.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^progressbarupload/?', include('progressbarupload.urls')),
    url(r'^$', RedirectView.as_view(pattern_name='test_form'))
]
