from tokenize import String
from django.db import models

# Create your models here.
class Projeto (models.Model):

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=50)
    dataInicio = models.DateField()
    dataFim = models.DateField()

    def __str__(self):
        return self.nome
    
class Coordenador (models.Model):

    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    whatsapp = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
class Professor (models.Model):

    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    whatsapp = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Empresa (models.Model):

    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    whatsapp = models.BooleanField(default=False)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    