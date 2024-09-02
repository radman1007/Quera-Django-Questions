from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, TeamForm
from django.contrib.auth import login, authenticate, logout
from .models import User, Team
from django.contrib.auth.decorators import login_required

@require_http_methods(["GET"])
def home(request):
    if request.user.is_authenticated:
        if request.user.account.team: 
            team = request.user.account.team.name
        else:
            team = None
        context = {
            'team' : team,
        } 
    else:
        context = {
            'team' : None,
        }
    return render(request, 'home.html', context)

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "GET":
        form = SignUpForm()
        context = {
            'form' : form
        }
        return render(request, 'signup.html', context)
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('team')
        else:
            context = {
                 'form' : form,
                 'errors' : form.errors,
            }
            return render(request, 'signup.html', context)
            

@require_http_methods(["GET", "POST"])
def login_account(request):
    if request.method == "GET":
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request, 'login.html', context)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data['username']).first()
            if user == None:
                return redirect('login')
            user = authenticate(username=user, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            else:
                return redirect('login')
        else:
            return redirect('login')

@require_http_methods(["GET"])
def logout_account(request):
    logout(request)
    return redirect('login')

@login_required
@require_http_methods(["GET", "POST"])
def joinoradd_team(request):
    if request.method == "GET":
        if request.user.account.team:
            return redirect('home')
        context = {
            'form' : TeamForm(),
        }
        return render(request, 'team.html', context)
            
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team_name = form.cleaned_data['name']
            jitsi_url_path = f"http://meet.jit.si/{team_name}"
            team, created = Team.objects.get_or_create(name=team_name, defaults={'jitsi_url_path': jitsi_url_path})
            request.user.account.team = team
            request.user.account.save()
            return redirect('home')
        else:
            return redirect('home')

@login_required
@require_http_methods(["GET"])
def exit_team(request):
    if request.user.account.team:
        request.user.account.team = None
        request.user.account.save()
    return redirect('home')
    