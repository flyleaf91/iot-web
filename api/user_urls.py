from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url('^reg/', 'api.user_views.register'),
    url('^login/', 'api.user_views.login'),
)
