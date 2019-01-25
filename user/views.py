from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form,
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.warning(request,"Kullanıcı adı veya şifre yanlış")
            return render(request, 'user/login.html',context)

        messages.success(request,"Başarıyla giriş yapıldı")
        login(request,user)
        return redirect("index")
    return render(request, "user/login.html",context)

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Hoşgeldin {}".format(newUser.username))
        return redirect('index')

    context = {
    "form":form
    }
    return render(request, 'user/register.html',context)


def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı")
    return redirect('index')
