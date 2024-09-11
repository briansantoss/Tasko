from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("O nome Inserido já consta  na base de dados!")

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse("cadastro feito")


