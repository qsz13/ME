from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def write(request):
    if request.method == "GET":
        return HttpResponse(render(request, 'writeBlog.html'))
    elif request.method == "POST":
        title = request.POST["email"]
        content = request.POST["content"]

        pass



def timeline(request):

    return HttpResponse(render(request, 'blog.html'))
