from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import search_history , tweets, index , update, preProcess, topics, sentiments, emotion

urlpatterns = patterns('',
    (r'^history/$', search_history),
    (r'^tweets/$',tweets),
    (r'^index/$',index),
    (r'^update/$',update),
    (r'^tweetPreProcess/$',preProcess),
    (r'^topics/$',topics),
    (r'^sentiments/$',sentiments),
    (r'^emotion/$',emotion),
    # Examples:
    # url(r'^$', 'sentiment_vis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
)
