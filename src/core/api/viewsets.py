from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from  .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True) 
    
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
        return super().updade(request, *args, **kwargs)

    # PATH
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


   