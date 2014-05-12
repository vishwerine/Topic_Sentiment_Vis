from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import current_datetime , tweets, index

urlpatterns = patterns('',
    (r'^time/$', current_datetime),
    (r'^tweets/$',tweets),
    (r'^index/$',index),
    # Examples:
    # url(r'^$', 'sentiment_vis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
)
