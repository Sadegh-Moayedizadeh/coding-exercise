from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from typing import Optional

from .models import Account
from .forms import SignUpForm


def home(request: HttpRequest) -> HttpResponse:
    team = Account.objects.get(id=request.user.id).team
    if team is None:
        return render(request, 'home.html', context={'team': 'None'})
    return render(request, 'home.html', context={'team': team.name})


def signup(request: HttpRequest) -> Optional[HttpResponse]:
    if request.method == 'GET':
        return render(request, 'signup.html', context={'form': SignUpForm()})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('team/')
        HttpResponseRedirect('signup/')


def login_account(request):
    pass


def logout_account(request):
    pass


@login_required
def joinoradd_team(request):
    pass


def exit_team(request):
    pass
