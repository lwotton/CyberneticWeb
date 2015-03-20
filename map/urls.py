from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import render
from map.views import Index

urlpatterns = patterns('',
	# ex: /polls/
    url(r'^$', Index.as_view(), name='index'),
)