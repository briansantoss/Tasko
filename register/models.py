from django.db import models

# Definindo a estrutura da tabela dos usuários no banco de dados
# Campos: id, nome e senha


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    passwd = models.CharField(max_length=100, blank=False, null=False)
