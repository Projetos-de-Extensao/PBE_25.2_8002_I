from rest_framework import serializers
from .models import Proposta, Projeto, Coordenador, Professor, Empresa

class PropostaSerializer(serializers.ModelSerializer):
    teste = serializers.CharField(source='situacao', read_only=False)
    class Meta:
        model = Proposta
        fields = '__all__'
    
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request', None)
        
        if request and request.user:
            user = request.user
            
            # Se o usuário NÃO tiver permissão de escrita
            if not (user.is_superuser or user.groups.filter(name='Empresa').exists()):
                
                # Torna o campo somente leitura na entrada (POST, PUT, PATCH)
                # O campo continua visível na saída (GET), mas não pode ser modificado.
                fields['teste'].read_only = True 
                
        return fields

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'