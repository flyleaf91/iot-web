from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^lockinfo/', include('api.lockinfo_urls')),
)