from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.views.generic import TemplateView


def home(request):

    return HttpResponse(render(request, 'index.html'))
