# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.views',
    url(r'^list/$', 'list', name='list'),
)