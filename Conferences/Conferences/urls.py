from django.conf.urls import patterns, include, url
from Conferences.views import GenerateConfPage

urlpatterns = patterns('',
    url(r'^Conferences/$', GenerateConfPage),
)