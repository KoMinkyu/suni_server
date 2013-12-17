from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from suni_server.restapi import views as api_views

urlpatterns = patterns('',
    url(r'^test/?$', api_views.TestAPI.as_view(), name='test_api'),
    url(r'^nexttest/?$', api_views.TestAPI2.as_view()),
)
