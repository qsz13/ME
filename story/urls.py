from django.conf.urls import patterns, url
from story.views import *


urlpatterns = patterns('',

    url(r'^write/$', write),
    url(r'^write/achievement/', write_achievement),




)
