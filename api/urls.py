from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views',
    url(r'^lockinfo/', include('api.lockinfo_urls')),
    url(r'^user/', include('api.user_urls')),
    url('^demo_post/$', 'demo_post'),
)
