from rest_framework import  serializers
from .models import Usuario,   Gerenciamento , Projeto

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome', 'email')
    
    
class ProjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ('codigoProj','nomeProj','descProj','dtCadastro',)

class GerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerenciamento
        fields = ('valorOrcamento','valorGasto')