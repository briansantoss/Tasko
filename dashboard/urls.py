from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('logout/', views.dash_logout, name='logout'),
]
