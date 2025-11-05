from django.contrib import admin

from .models import Proposta, Projeto, Coordenador, Professor, Empresa

class PropostaAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)

        if request.user.groups.filter(name="Empresa").exists():
            fields = [f for f in fields if f != 'situacao']

        return fields

class ProjetoAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "proposta":
            kwargs["queryset"] = Proposta.objects.filter(situacao="Aprovada")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Proposta, PropostaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Coordenador)
admin.site.register(Professor)
admin.site.register(Empresa)
