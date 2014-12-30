import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from friends.exceptions import AlreadyExistsError
from friends.models import Friend
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from notifications import notify


user_model = get_user_model()
get_friendship_context_object_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_NAME', 'user')


@login_required
def view_friends(request):
    template_name = 'friends.html'
    user = get_object_or_404(user_model, username=request.user)
    friends = Friend.objects.friends(user)
    return HttpResponse(
        render(request, template_name, {get_friendship_context_object_name(): user, 'friends': friends}))


@login_required
def add_friends(request):
    """ Create a FriendshipRequest """
    response_data = {}
    if request.method == 'POST':
        to_user_email = request.POST['email']
        message = request.POST['message']
        from_user = request.user
        try:
            to_user = user_model.objects.get(username=to_user_email)
        except ObjectDoesNotExist as e:
            response_data['success'] = False
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        Friend.objects.add_friend(from_user, to_user, message)
        response_data['success'] = True
        return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required
def writing_invite(request):
    response_data = {}
    if request.method == 'POST':
        to_user_id = request.POST['user_id']
        title = request.POST['title']
        message = request.POST['message']
        from_user = request.user
        to_user = user_model.objects.get(id=to_user_id)
        print to_user.username

        notify.send(from_user, recipient=to_user, verb=title,
            description=message)
        response_data['success'] = True
        return HttpResponse(json.dumps(response_data), content_type="application/json")

