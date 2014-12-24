from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):

    if request.user.is_authenticated():
        # return HttpResponseRedirect("/login/")
        return HttpResponse(render(request, 'blog.html'))

    else:
        return HttpResponse(render(request, 'index.html'))
