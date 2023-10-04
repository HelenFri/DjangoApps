from django.contrib import messages
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

