from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user = auth.authenticate(username=username, password=password)
        if check_user == None:
            messages.error(request, message='Usuário e/ou senha inválido(s)!')
            return redirect('login')
        else:
            auth.login(request, check_user)
            return redirect('home')
    else:
        return render(request, 'pages/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastrar(request):

    if request.method == 'POST':
        # user = request.POST['username']
        user = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        User.objects.create_user(username=user, email=email, password=password)
        return redirect('login')
    else:
        return render(request, 'pages/cadastrar.html')
