from django.contrib import admin

from .models import Proposta, Projeto, Coordenador, Professor, Empresa

admin.site.register(Proposta)
admin.site.register(Projeto)
admin.site.register(Coordenador)
admin.site.register(Professor)
admin.site.register(Empresa)
