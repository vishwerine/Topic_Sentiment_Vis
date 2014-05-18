from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import search_history , tweets, index

urlpatterns = patterns('',
    (r'^history/$', search_history),
    (r'^tweets/$',tweets),
    (r'^index/$',index),
    # Examples:
    # url(r'^$', 'sentiment_vis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
)
