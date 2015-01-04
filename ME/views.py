from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from story.models import Story


def home(request):

    if request.user.is_authenticated():

        stories = Story.objects.filter(Q(author=request.user) | Q(owner=request.user)).select_subclasses().order_by("-time")




        return HttpResponse(render(request, 'home.html', {'stories':stories}))

    else:
        return HttpResponse(render(request, 'index.html'))
