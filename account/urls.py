__author__ = 'danielqiu'
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import register
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
   # url(r'^succes/$', TemplateView.as_view(template_name="user/succes.html")),
    url(r'^register/$', register),
    #url(r'^login/$', login, {'template_name': 'user/login.html'}),
    #url(r'^logout/$', logout, {'next_page' : '/user/login'}),
    #url(r'^profile/$', login_required(TemplateView.as_view(template_name="user/profile.html"))),
)