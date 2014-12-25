from django.conf.urls import patterns, url
from story.views import *


urlpatterns = patterns('',

    url(r'^timeline/', timeline),
    url(r'^write/', write),
)
