from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import NewUser, Note


def home(request):
    return render(request, 'mainapp/home.html', context={'page': home})


def reg(request):
    if request.method == 'GET':
        return render(request, 'mainapp/reg.html')

    if request.user.is_anonymous:
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
    else:
        messages.info(request, f'Пользователь {request.user} уже зарегистрирован.')
        return redirect(reg)

    return render(request, 'mainapp/reg.html', context={'page': reg})


def login_page(request):
    if request.method == 'GET':
        return render(request, 'mainapp/login.html', context={'page': login})

    if request.user.is_anonymous:
        data = request.POST
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            messages.error(request, f'Пользователь с такими логином и паролем не найден.')
            return redirect(login_page)
        else:
            login(request, user)
            messages.success(request, f'Вы успешно авторизованы.')
            return redirect(home)
    else:
        messages.info(request, f'Пользователь {request.user} уже авторизован.')
        return redirect(home)


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, f'Вы вышли из аккаунта.')
        return redirect(home)

    messages.info(request, f'Вы не авторизованы.')
    return redirect(home)


def notes(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(User=request.user).all()
        return render(request, 'mainapp/notes.html', context={'notes': notes})

    messages.info(request, f'Войдите в аккаунт, чтобы просматривать свои заметки.')
    return redirect(login_page)


def add_note(request):
    if request.method == 'GET':
        return render(request, 'mainapp/add_note.html')

    if request.user.is_authenticated:
        data = request.POST
        txt = data.get('note-text')
        note = Note()
        note.create_note(txt, request.user)
        messages.info(request, f'Заметка добавлена.')
        return redirect(add_note)

    messages.info(request, f'Войдите в аккаунт, чтобы добавлять заметки.')
    return redirect(login_page)
