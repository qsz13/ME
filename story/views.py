from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from story.models import *
import datetime
# Create your views here.

def write(request):
    if request.method == "GET":
        return HttpResponse(render(request, 'choose_write_type.html'))
    elif request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        now = datetime.datetime.now()
        mood = ""
        story = Story.objects.create(title=title, content=content, time=now, mood=mood)
        story.save()
        return HttpResponseRedirect("/")



def write_achievement(request):
    return HttpResponse(render(request, 'write_achievement.html'))
