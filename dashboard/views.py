from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Task
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    task = Task.objects.create(title='Acordar', description='Acordar mano, preciso', username_id=1)
    return render(request, 'dashboard/dashboard.html')


def dash_logout(request):
    logout(request)
    return redirect('home')
