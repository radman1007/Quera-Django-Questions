from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, TeamForm
from django.contrib.auth import login, authenticate
from .models import User, Team
from django.contrib.auth.decorators import login_required

@require_http_methods(["GET"])
def home(request):
    if request.user.is_authenticated:
        if request.user.team: 
            team = request.user.team.name
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
            form.save()
            login(request, form.username, backend='django.contrib.auth.backends.ModelBackend')
            redirect('team')
        else:
            redirect('signup')
            

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
            user = User.objects.filter(username=form.username).first()
            if user == None:
                return redirect('login')
            user = authenticate(username=user, password=form.password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                redirect('home')
            else:
                redirect('login')
        else:
            redirect('login')

def logout_account(request):
    pass


@login_required
@require_http_methods(["GET", "POST"])
def joinoradd_team(request):
    if request.method == "GET":
        if request.user.team:
            return redirect('home')
        context = {
            'form' : TeamForm(),
        }
        return render(request, 'team.html', context)
            
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(name=form.name).first()
            if team == None:
                new_form = form.save(commit=False)
                new_form.jitsi_url_path = f'http://meet.jit.si/{new_form.name}'
                new_form.save()
                request.user.team = new_form
                request.user.save()
                return redirect('home')
            else:
                request.user.team = team
                request.user.save()
                return redirect('home')
        else:
            return redirect('home')

@login_required
@require_http_methods(["GET"])
def exit_team(request):
    if request.user.team:
        request.user.team = None
        request.user.save()
    return redirect('home')
    