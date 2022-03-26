from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_IsValid(data['cpf']):
            raise serializers.ValidationError({'cpf':"Digite um CPF válido!"})
        if not nome_IsValid(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua números neste campo!"}) 
        if not rg_IsValid(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 digitos!"})
        if not celular_IsValid(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir este modelo: 11 91111-1111"})
        return data
    
    
    
    
   
    
    