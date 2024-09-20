from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, 'register/register.html')

    nome_usuario = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('password')

    user = User.objects.filter(username=nome_usuario).first()
    if user:
        return render(request, 'register/register.html', {'usuario_existe': True})

    user = User.objects.create_user(username=nome_usuario, email=email, password=senha)
    return render(request, 'login/login.html')
