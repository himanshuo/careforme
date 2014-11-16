from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weallcare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # (r'^facebook/', include('django_facebook.urls')),
    # (r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.

    url(r'^$','login.views.home', name='home' ),
    url(r'^facebook_login$','login.views.facebook_login', name='facebook_login' ),
    url(r'^member$','login.views.member', name='member'),
)
