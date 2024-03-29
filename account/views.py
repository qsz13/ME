import json
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile, File
from django.core.files.storage import FileSystemStorage, default_storage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from ME import settings
from account.models import Profile
from emailusernames.forms import EmailUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from friends.models import FriendshipRequest, Friend



def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['email'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "/")

def register_sub(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['email'],
                                    password=request.POST['password1'])
            new_user.profile.parent_account = request.user.profile
            new_user.profile.save()
            print new_user.profile.parent_account
            return HttpResponseRedirect("/account/sub_account/")
        else:
            print form.error_messages
            return HttpResponseRedirect("/account/sub_account/")




def account(request):
    return HttpResponse(render(request, 'account.html'))


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/disabled_account")
        else:
            return HttpResponseRedirect("/invalid_login")


def signout(request):
    logout(request)
    return HttpResponseRedirect("/")


def sub_account(request):

    user = request.user
    sub = user.profile.child_account.all()


    return HttpResponse(render(request, 'sub_account.html',{'sub_accounts':sub}))


@login_required
def setting(request):
    template_name='personalInfo.html'
    requests = Friend.objects.requests(request.user)
    user_image = request.user.profile.avatar

    return HttpResponse(render(request, template_name, {'friendship_requests': requests, 'user_image': user_image, 'notifications': request.user.notifications.all()}))



@login_required
def friends_reject(request, friendship_request_id):
    """ Reject a friendship request """
    response_data = {}
    if request.method == 'GET':
        try:
            f_request = request.user.friendship_requests_received.get(id=friendship_request_id)
        except ObjectDoesNotExist as e:
            response_data['success'] = False
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        f_request.reject()
        response_data['success'] = True
        return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required
def friends_accept(request, friendship_request_id):
    """ Accept a friendship request """
    response_data = {}
    if request.method == 'GET':
        try:
            f_request = request.user.friendship_requests_received.get(id=friendship_request_id)
        except ObjectDoesNotExist as e:
            response_data['success'] = False
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        f_request.accept()
        response_data['success'] = True
        return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required
def change(request):
    if request.method == 'POST':
        user = request.user
        if 'avatar' in request.FILES:
            data = request.FILES['avatar']
            type = str.split('.',str(data))[-1]
            file_path = os.path.join("avatar", str(user.id)+'.'+type)
            file_real_path = default_storage.save(file_path, ContentFile(data.read()))
            user.profile.avatar = file_real_path
            user.profile.save()
        if request.POST['username'] is not u"":
            user.username = request.POST['username']
            user.save()
        if request.POST['phone'] is not u"":
            user.profile.phone = request.POST['phone']
        if request.POST['password'] is not u"":
            user.set_password(request.POST['password'])

        user.save()
        user.profile.save()
        return HttpResponseRedirect("/account/setting/")


def remove_sub(request, profile_id):
    if request.method == "GET":
        profile = Profile.objects.get(id=profile_id)
        profile.parent_account = None
        profile.save()
    return HttpResponseRedirect("/account/sub_account/")



def remove_account(request, profile_id):
    if request.method == "GET":
        profile = Profile.objects.get(id=profile_id)
        profile.parent_account = None
        profile.save()
    return HttpResponseRedirect("/account/sub_account/")