from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    username = request.POST.get('username')
    senha = request.POST.get('password')

    user = authenticate(username=username, password=senha)
    if user:
        login_django(request, user)
        return redirect('dashboard')
    return render(request, 'login/login.html', {'erro_login': True})
