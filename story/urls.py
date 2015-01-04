from django.conf.urls import patterns, url
from story.views import *


urlpatterns = patterns('',

    url(r'^write/$', write),
    url(r'^write_achievement', write_achievement),
    url(r'^write_activityMemory', write_activityMemory),
    url(r'^write_growth', write_growth),
    url(r'^write_travel', write_travel),
    url(r'^write_meaning', write_meaning),
    url(r'^write_note', write_note),
    url(r'^view/(?P<story_id>\d+)/', view_story),





)
