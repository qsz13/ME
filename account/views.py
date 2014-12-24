from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
# Create your views here.
from emailusernames.forms import EmailUserCreationForm

def register(request):

    if request.method == 'POST':
        print "asdfasdf"
        form = EmailUserCreationForm(request.POST)
        print form.errors
        if form.is_valid():
            print "asdkjfhasfkj"
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
        return render(request, "/")