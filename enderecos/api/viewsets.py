from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer
from rest_framework.pagination import PageNumberPagination

class EnderecoPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    pagination_class = EnderecoPagination