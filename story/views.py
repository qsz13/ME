# -*- coding: utf-8 -*- #
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from story.models import *
import datetime
# Create your views here.

def write(request):
    if request.method == "GET":
        return HttpResponse(render(request, 'choose_write_type.html'))


def write_achievement(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'privateAchievement.html'))
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        mood = request.POST['mood']
        img = save_image(request)
        author = request.user
        Achievement.objects.create_achievement(author,title, content, mood, img)

        return HttpResponseRedirect("/")


def write_activityMemory(request):
    if request.method=='GET':
        return HttpResponse(render(request, 'activityMemory.html'))
    elif request.method=='POST':
        title = request.POST['title']
        content = request.POST['content']
        mood = request.POST['mood']
        author = request.user
        place = request.POST['place']
        together_with = request.POST['together_with']
        img = save_image(request)
        Activity.objects.create_activity(author, title, content, mood, together_with, place, img)
        return HttpResponseRedirect("/")



def write_growth(request):
    if request.method == "GET":
        return HttpResponse(render(request, 'growth.html'))
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        mood = request.POST['mood']
        author = request.user
        age = request.POST['age']
        weight = request.POST['weight']
        height = request.POST['height']
        img = save_image(request)
        Growth.objects.create_growth(author, title, content, mood, age, weight, height, img)

def write_travel(request):
    return HttpResponse(render(request, 'travel.html'))



def write_meaning(request):
    if request.method == "GET":
        return HttpResponse(render(request, 'meaning.html'))
    elif request.method == "POST":
        title = request.POST['title']
        return HttpResponseRedirect("/")




def write_note(request):
    return HttpResponse(render(request, 'note.html'))



def view_story(request, story_id):
    if request.method=="GET":
        story = Story.objects.filter(id=story_id).select_subclasses()[0]
        type = u''
        print isinstance(story, Achievement)
        print story.mood
        if isinstance(story, Achievement):
            type = u'个人成就'
        if isinstance(story, Activity):
            type = u'活动经历'
        if isinstance(story, Growth):
            type = u'成长纪录'
        return HttpResponse(render(request, 'blog-single.html', {'story': story, 'type': type}))





def save_image(request):
    if 'image' in request.FILES:
        data = request.FILES['image']
        type = str.split('.', str(data))[-1]
        file_path = os.path.join("upload", str(request.user.id)+'.'+type)
        file_real_path = default_storage.save(file_path, ContentFile(data.read()))
        return file_real_path
    else:
        return ""