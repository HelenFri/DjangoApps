from django.shortcuts import render


def home(request):
    return render(request, 'mainapp/home.html', context={'page': home})

