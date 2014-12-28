__author__ = 'danielqiu'
from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',

    url(r'^register/$', register),
    url(r'^signin/$', signin),

    url(r'^$',account),
    url(r'^sub_account/$',sub_account),


)