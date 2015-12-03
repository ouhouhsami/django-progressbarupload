from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'testapp.views.home', name='home'),
    url(r'^testapp/', include('testmain.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^progressbarupload/', include('progressbarupload.urls')),
]
