from django.db import models
from django.contrib.auth.models import User


class Dados(models.Model):
    
    nome = models.CharField(max_length=100)
    cpf=models.CharField(max_length=50)
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enderecos')
    descricao = models.CharField(max_length=100)
   

    def __str__(self):
        return self.descricao








