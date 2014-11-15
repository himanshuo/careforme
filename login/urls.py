from django.conf.urls import patterns, include, url
from django.contrib import admin


__author__ = 'himanshu'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weallcare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$','login.views.home', name='home' ),
    url(r'^test','login.views.test', name='test' ),

)