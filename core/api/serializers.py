from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import PontoTuristico

class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao')