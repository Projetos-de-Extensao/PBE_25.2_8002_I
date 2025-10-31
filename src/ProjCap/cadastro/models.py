from tokenize import String
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Proposta(models.Model):

    expectativa_escolhas= [
    ('6 meses', '6 meses'),
    ('9 meses', '9 meses'),
    ('1 ano', '1 ano'),
    ('Não tenho expectativa', 'sem expectativa'),
    ]

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

    vinculo_escolhas= [
    ('Aluno / Ex-aluno IBMEC', 'Aluno / Ex-aluno IBMEC'),
    ('faço parte do IBMEC HUBS', 'faço parte do IBMEC HUBS'),
    ('Não tenho vínculo com o IBMEC', 'Não tenho vínculo com o IBMEC')
    ]    
    status_proposta = [
    ('Em análise', 'Em análise'),
    ('Recusada', 'Recusada'),
    ('Aprovada', 'Aprovada')
    ]
    
    nomeSolucao = models.CharField("Nome da Solução", max_length=100, blank=False)
    objetivo = models.TextField(blank=False)
    tecnologias = models.TextField(blank=False)
    representante = models.CharField(max_length=100, default='', blank=False)
    email = models.EmailField(max_length=100, default='', blank=False)
    telefone = PhoneNumberField(
        max_length=15,
        null=False,
        blank=False,
        region="BR",  # Define o país padrão (Brasil)
        help_text="Número de telefone no formato internacional (ex: +5511987654321)"
    )
    whatsapp = models.BooleanField("É whatsapp?", default=False)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, default=None)
    expectativa = models.CharField(
        max_length=21,
        choices=expectativa_escolhas,
        default='6 meses'
    )
    vinculoIbmec = models.CharField(
        "Possui vínculo com o IBMEC?", 
        max_length=100, 
        default='Não tenho vínculo com o IBMEC', 
        choices=vinculo_escolhas)
    situação = models.CharField(
        max_length=20,
        choices=status_proposta,
        default='Em análise'
    )

    def __str__(self):
        return self.nomeSolucao

class Projeto (models.Model):

    status= [
    ('Em andamento', 'Em andamento'),
    ('Concluído', 'Concluído')
    ]   
    
    nome = models.CharField(max_length=100, blank=False)
    descricao = models.TextField(blank=False)
    status = models.CharField(choices=status, max_length=50, blank=False, default='Em andamento')
    dataInicio = models.DateField(blank=False)
    dataFim = models.DateField(blank=False)
    coordenador = models.ForeignKey('Coordenador', on_delete=models.CASCADE, default=None)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, default=None)
    proposta = models.ForeignKey('Proposta', on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.nome
    
class Coordenador (models.Model):

    nome = models.CharField(max_length=100, blank=False)
    matricula = models.CharField(max_length=12, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    telefone = PhoneNumberField(
        default='',
        blank=False,
        region="BR",  # Define o país padrão (Brasil)
        help_text="Número de telefone no formato internacional (ex: +5511987654321)"
    )

    def __str__(self):
        return self.nome
    
class Professor (models.Model):

    nome = models.CharField(max_length=100, blank=False)
    matricula = models.CharField(max_length=12, blank=False)
    email = models.EmailField(max_length=100, blank=False)

    def __str__(self):
        return self.nome

class Empresa (models.Model):

    nome = models.CharField("Nome da Empresa", max_length=100, blank=False)
    cnpj = models.CharField("CNPJ", max_length=14, blank=False)
    endereco = models.TextField("Endereço", blank=False)
    email = models.EmailField("E-mail", max_length=100, blank=False)
    telefone = PhoneNumberField(
        "Telefone",
        blank=False,
        region="BR",  # Define o país padrão (Brasil)
        help_text="Número de telefone no formato internacional (ex: +5511987654321)"
    )
    whatsapp = models.BooleanField("É whatsapp?", default=False)
    observacoes = models.TextField("Observações", blank=False, default='Nenhuma')

    def __str__(self):
        return self.nome
    