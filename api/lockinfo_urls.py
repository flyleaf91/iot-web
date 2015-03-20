from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url('^add/', 'api.lockinfo_views.add_lockinfo'),
    url('^list/', 'api.lockinfo_views.list_lockinfo'),
)