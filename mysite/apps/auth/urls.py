# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from .views import auth_login

urlpatterns = patterns('',
    url(r'^login/$', auth_login, name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'auth/logout.html'}, name='auth_logout'),
)