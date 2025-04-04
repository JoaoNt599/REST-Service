import django_filters
from avaliacoes.models import Avaliacao

class AvaliacaoFilter(django_filters.FilterSet):
    comentario = django_filters.CharFilter(lookup_expr='icontains') 
    
    class Meta:
        model = Avaliacao
        fields = ['comentario', 'nota', 'user', 'data']
