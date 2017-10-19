#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^app/(\d+)/$', views.detalle_aplicativo, name='detalle_aplicativo'),
    ]
