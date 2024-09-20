from django.contrib.auth.models import User
from django.db import models

# Definindo a estrutura (campos e suas restrições/características) da tabela de tarefas
# Campos: id (predefinido), título, descrição e um status


class Task(models.Model):
    # Definindo uma lista de tuplas que vai determinar os valores que o campo 'status' vai poder assumir na tabela
    CHOICES = [('em_andamento', 'Em andamento'), ('concluida', 'Concluída')]

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    status = models.CharField(max_length=100, choices=CHOICES, default='em_andamento', null=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
