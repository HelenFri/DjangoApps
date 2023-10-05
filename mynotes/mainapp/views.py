from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import NewUser


def home(request):
    return render(request, 'mainapp/home.html', context={'page': home})


def reg(request):
    if request.method == 'GET':
        return render(request, 'mainapp/reg.html')

    data = request.POST
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    pas1 = data.get('password1')
    new_user = NewUser()
    new_user.create_user(username, first_name, last_name, email, pas1)
    if new_user:
        messages.success(request, f'Регистрация завершена успешно. Создан аккаунт {username}.')
        return redirect(reg)

    return render(request, 'mainapp/reg.html', context={'page': reg})


def login_page(request):
    if request.method == 'GET':
        return render(request, 'mainapp/login.html', context={'page': login})

    data = request.POST
    user = authenticate(request, username=data['username'], password=data['password'])

    if user is None:
        messages.error(request, f'Пользователь с такими логином и паролем не найден.')
        return redirect(login_page)
    else:
        login(request, user)
        messages.success(request, f'Вы успешно авторизованы.')
        return redirect(home)


def logout_page(request):
    logout(request)
    messages.info(request, f'Вы успешно вышли из аккаунта')
    return redirect(home)
