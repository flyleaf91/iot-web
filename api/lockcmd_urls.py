from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url('^add/', 'api.lockcmd_views.add_lockcmd'),
    url('^get/', 'api.lockcmd_views.get_latest_cmd'),
)
