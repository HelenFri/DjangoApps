from django.shortcuts import render


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
    pas1, pas2 = data.get('password1'), data.get('password2')

    return render(request, 'mainapp/reg.html', context={'page': reg})

