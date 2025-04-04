import django_filters
from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AvaliacaoFilter

class AvaliacaoPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100


class AvaliacaoFilter(django_filters.FilterSet):
    comentario = django_filters.CharFilter(field_name="comentario", lookup_expr="icontains")
    nota = django_filters.NumberFilter(field_name="nota")
    data = django_filters.DateTimeFilter(field_name="data")

    class Meta:
        model = Avaliacao
        fields = ["user", "comentario", "nota", "data"]

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all().order_by('id')
    serializer_class = AvaliacaoSerializer
    pagination_class = AvaliacaoPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AvaliacaoFilter