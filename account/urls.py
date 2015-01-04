__author__ = 'danielqiu'
from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',



    url(r'^$',account),
    url(r'^sub_account/$',sub_account),
    url(r'^setting/$',setting),
    url(r'^setting/friends-reject/(?P<friendship_request_id>\d+)/$', friends_reject),
    url(r'^setting/friends-accept/(?P<friendship_request_id>\d+)/$', friends_accept),
    url(r'^register/$', register),
    url(r'^register_sub/$', register_sub),

    url(r'^signin/$', signin),
    url(r'^signout/$', signout),
    url(r'^setting/change$', change),
    url(r'^remove_sub/(?P<profile_id>\d+)/$',remove_sub),
    url(r'^remove_account/(?P<profile_id>\d+)/$',remove_account),


)