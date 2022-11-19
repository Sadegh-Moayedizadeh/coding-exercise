from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from typing import Optional

from .models import Account, Team
from .forms import SignUpForm, LoginForm, TeamForm


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
            return HttpResponseRedirect('/account/team/')
        HttpResponseRedirect('/account/signup/')


def login_account(request: HttpRequest) -> Optional[HttpResponse]:
    if request.method == 'GET':
        return render(request, 'login.html', context={'form': LoginForm()})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_qs = Account.objects.filter(username=username)
            if user_qs.exists() and \
                    check_password(password, user_qs.first().password):
                login(request, user_qs.first())
                return HttpResponseRedirect('/home/')
        return HttpResponseRedirect('/account/login/')


def logout_account(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponseRedirect('/account/login/')


@login_required
def joinoradd_team(request: HttpRequest) -> HttpResponse:
    user_account = Account.objects.get(
        id=request.user.id
    )
    if request.method == 'GET':
        if user_account.team is None:
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponseRedirect('/home/')
            return render(request, 'team.html', context={'form': TeamForm()})
    elif request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team_name = form.cleaned_data.get('name')
            if Team.objects.filter(name=team_name).exists():
                user_account.team = Team.objects.get(name=team_name)
                user_account.save(update_fields=['team'])
            else:
                team = Team.objects.create(
                    name=team_name,
                    jitsi_url_path='http://meet.jit.si/{}'.format(team_name)
                )
                user_account.team = team
                user_account.save(update_fields=['team'])
        return HttpResponseRedirect('/home/')


def exit_team(request):
    if request.method == 'GET':
        user_account = Account.objects.get(
            id=request.user.id
        )
        user_account.team = None
        user_account.save(update_fields=['team'])
        return HttpResponseRedirect('/home/')
