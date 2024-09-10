from django.db import models

# Definindo a estrutura da tabela dos usuários no banco de dados
# Campos: id, título, descrição e um status


class Tasks(models.Model):
    # Definindo uma lista de tuplas que vai determinar os valores que o campo 'status' vai poder assumir na tabela
    CHOICES = [('em_andamento', 'Em andamento'), ('concluida', 'Concluída')]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    status = models.CharField(max_length=100, choices=CHOICES, default='em_andamento', null=False)
