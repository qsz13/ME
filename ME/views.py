from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    if request.user.is_authenticated():
        return HttpResponse(render(request, 'home.html'))

    else:
        return HttpResponse(render(request, 'index.html'))
