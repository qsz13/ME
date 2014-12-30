from django.conf.urls import patterns, url
from story.views import *


urlpatterns = patterns('',

    url(r'^write/$', write),
    url(r'^write/achievement/', write_achievement),
    url(r'^write/activityMemory', write_activityMemory),
    url(r'^write/growth', write_growth),
    url(r'^write/travel', write_travel),
    url(r'^write/meaning', write_meaning),
    url(r'^write/note', write_note),
    url(r'^view/(?P<story_id>\d+)/', view_story),





)
