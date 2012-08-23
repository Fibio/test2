# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from apps.auth.views import partner_login

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', login_required(direct_to_template),  {'template': 'index.html'}, name='index'),
    url(r'^accounts/', include('apps.auth.urls')),
    url(r'^partner/somepage', login_required(direct_to_template),
        {'template': 'another_page.html'}, name='some_view'), #for test
    url(r'^partner/login', partner_login, name='partner_login'),



    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
