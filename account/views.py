import json
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from emailusernames.forms import EmailUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from friends.models import FriendshipRequest, Friend


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        print form.errors
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['email'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "/")


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
    return HttpResponse(render(request, 'sub_account.html'))


@login_required
def setting(request):
    template_name='personalInfo.html'
    requests = Friend.objects.requests(request.user)

    return HttpResponse(render(request, template_name, {'friendship_requests': requests}))



@login_required
def friends_reject(request, friendship_request_id):
    """ Reject a friendship request """
    response_data = {}
    if request.method == 'GET':
        print friendship_request_id
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
        print friendship_request_id
        try:
            f_request = request.user.friendship_requests_received.get(id=friendship_request_id)
        except ObjectDoesNotExist as e:
            response_data['success'] = False
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        f_request.accept()
        response_data['success'] = True
        return HttpResponse(json.dumps(response_data), content_type="application/json")
