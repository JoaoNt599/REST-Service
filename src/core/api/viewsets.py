import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from core.models import PontoTuristico
from  .serializers import PontoTuristicoSerializer


class PontoTuristicoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='iexact')
    descricao = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = PontoTuristico
        fields = ['nome', 'descricao']

class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PontoTuristicoFilter

    def get_queryset(self):
        """
        Controle manual do filtro por ID
        """
        try:
            queryset = super().get_queryset()
            id = self.request.query_params.get('id', None)

            if id:
                if not id.isdigit():
                    raise ValidationError({"erro": "ID inválido. O ID deve ser um número inteiro."})
                queryset = queryset.filter(pk=id)

                if not queryset.exists():
                    raise ValidationError({"erro": "Nenhum ponto turístico encontrado com esse ID."})

            return queryset
        
        except ValidationError as err:
            raise err  
        
        except Exception as err:
            print(f"Erro inesperado em get_queryset: {err}")
            raise ValidationError({"erro": "Ocorreu um erro inesperado ao processar a requisição."})
       
    
    @action(methods=['post', 'get'], detail=True) #, permission_classes=[IsAtuthenticated]
    def denunciar(self, request, pk=None):
        atracao = self.get_object()
        return Response(
            {
                'mensagem': f'Atração {atracao.nome} denunciada com sucesso!'
            }
        )
    
    # GET
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # POST
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # DELETE
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # GET (Retrieve)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # PUT
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # PATH
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


   