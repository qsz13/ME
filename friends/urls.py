__author__ = 'danielqiu'
from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',

    url(r'^$', view_friends),
    url(r'^add/$', add_friends),
    url(r'^invite/$', writing_invite),


)
