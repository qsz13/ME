from django.shortcuts import render
from django.http import HttpResponseRedirect
from emailusernames.forms import EmailUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse



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