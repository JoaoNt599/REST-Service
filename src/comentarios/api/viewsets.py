from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class ComentarioPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

class ComentarioViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    pagination_class = ComentarioPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'usuario': ['exact'],
        'comentario': ['exact', 'icontains'],
        'data': ['exact', 'date'],
        'aprovado': ['exact'],
    }