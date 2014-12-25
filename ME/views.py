from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    if request.user.is_authenticated():
        return HttpResponse(render(request, 'blog.html'))

    else:
        return HttpResponse(render(request, 'index.html'))
