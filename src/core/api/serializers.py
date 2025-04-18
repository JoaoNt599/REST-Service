from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import PontoTuristico
import re
from core.validators.decorators import unique_validation, required_and_not_numeric, validate_put_fields, validate_patch_fields

class PontoTuristicoSerializer(serializers.ModelSerializer):

    nome = serializers.CharField(
        required=True,
        allow_blank=True
    )

    descricao = serializers.CharField(
        required=True,
        allow_blank=True
    )

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto')

    
    @required_and_not_numeric("nome")
    def validate_nome(self, value):
        return value


    @required_and_not_numeric("descricao")
    def validate_descricao(self, value):
        return value
    

    @unique_validation(PontoTuristico, ['nome', 'descricao'])
    def validate(self, data):
        return data
    

    @validate_put_fields(model=PontoTuristico, unique_fields=["nome", "descricao"])
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

    @validate_patch_fields(PontoTuristico, unique_fields=["nome", "descricao"])
    def partial_update(self, instance, validated_data):
        return super().update(instance, validated_data)

    
