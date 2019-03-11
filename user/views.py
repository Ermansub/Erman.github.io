from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Questions

# Create your views here.
def index(request):
    if request.user.username:
        wall = Questions.objects.all()
        data = {"title": request.user.username, "wall": wall}
    else:
        userform = UserForm()
        data = {"title": "Добро пожаловать", "form": userform}
        if request.method == "POST":
            login = request.POST.get("login")
            password = request.POST.get("password")
            user = auth.authenticate(username=login,password=password)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect("/")
            else:
                data['login_error'] = 'Пользователь не найден'
    return render(request, "index.html", data)

def registration(request):
    userform = UserCreationForm()
    data = {"title": "Добро пожаловать", "form": userform}
    if request.POST:
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            newUser = auth.authenticate(username=new_user.cleaned_data['username'], password=new_user.cleaned_data['password2'])
            auth.login(request, newUser)
            return HttpResponseRedirect("/")
        else:
            data['form'] = new_user
    return render(request, "registration.html", data)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def users(request):
    users = User.objects.all()
    data = {"title": "Список пользователей", "users": users}
    return render(request, "users.html", data)

def profile(request, userid):
    user = User.objects.get(id=userid)
    data = {"title": "Профиль", "user_page": user}
    return render(request, "profile.html", data)
