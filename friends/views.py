from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from friends.models import Friend
from django.contrib.auth import get_user_model
from django.conf import settings

user_model = get_user_model()
get_friendship_context_object_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_NAME', 'user')



@login_required
def view_friends(request):
    user = get_object_or_404(user_model, username=request.user)
    friends = Friend.objects.friends(user)
    print friends
    return HttpResponse(render(request, 'friends.html', {get_friendship_context_object_name(): user, 'friends': friends}))

