from tokenize import String
from django.db import models
from django import forms

# Create your models here.
class Proposta(models.Model):
    nomeSolucao = models.CharField("Nome da Solução", max_length=100)
    objetivo = models.TextField()
    tecnologias = models.TextField()

    expectativa_escolhas= [
    ('6 meses', '6 meses'),
    ('9 meses', '9 meses'),
    ('1 ano', '1 ano'),
    ('Não tenho expectativa', 'sem expectativa'),
    ]
    expectativa = models.CharField(
        max_length=21,
        choices=expectativa_escolhas,
        default='6 meses'
    )
    vinculo_escolhas= [
    ('Aluno / Ex-aluno IBMEC', 'Aluno / Ex-aluno IBMEC'),
    ('Faço / faço parte do IBMEC HUBS', 'Faço / faço parte do IBMEC HUBS'),
    ('Índio não ter vínculo com IBMEC', 'Índio não ter vínculo com IBMEC')
    ]
    vinculoIbmec = models.CharField(
        "Possui vínculo com o IBMEC?", 
        max_length=100, 
        default='Índio não ter vínculo com IBMEC', 
        choices=vinculo_escolhas)

    representante = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)
    whatsapp = models.BooleanField("É whatsapp?", default=False)

    tipo_escolhas= [
    ('Front-End', 'Front-End'),
    ('Back-End', 'Back-End'),
    ('Mobile', 'Mobile'),
    ('Projeto de Bi', 'Projeto de Bi'),
    ('Sistemas Embarcados', 'Sistemas Embarcados'),
    ('Cloud', 'Cloud')
    ]
    tipoSistema = models.CharField(
        "Tipo do Sistema",
        max_length=50,
        choices=tipo_escolhas,
        default='Front-End'
    )


    def __str__(self):
        return self.titulo

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
    