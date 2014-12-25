from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def view_friends(request):
    return HttpResponse(render(request, 'friends.html'))
